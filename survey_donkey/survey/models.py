from django.db import models
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import JSONField

from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
import uuid


def get_expiration_date():
    """
    Returns the current time plus 24 hours.

    Returns:
        datetime: The current time plus 24 hours.
    """
    return timezone.now() + timedelta(hours=24)

def get_expiration_date_week():
    """
    Return the current time plus 1 week.
    
    Returns:
        datetime: The current time plus 1 week.
    
    """
    return timezone.now() + timedelta(days=7)

def get_current_time():
    """
    Returns the current time.

    Returns:
        datetime: The current time.
    """
    return timezone.now()

class CustomUserManager(BaseUserManager):
    def create_user(self, email, **extra_fields):
        """
        Creates and saves a User with the given email.

        Args:
            email (str): The email of the user.
            **extra_fields: Extra fields to be saved with the user.

        Raises:
            ValueError: If no email is provided.

        Returns:
            User: The user that was created.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        password = extra_fields.get('password')
        if password:
            user.password = make_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user
    
    def create_login_token(self, email):
        """
        Creates a unique login token for a user.

        Args:
            email (str): The email of the user.

        Raises:
            ValueError: If no user with the given email exists.

        Returns:
            str: The login token.
        """
        try:
            user = self.get(email=email)
            token = uuid.uuid4()
            expiration_date = get_expiration_date_week()
            # Save the token and expiration date in the user model
            user.login_token = str(token)
            user.login_token_expiration = expiration_date
            user.save()
            return str(token)
        except self.model.DoesNotExist:
            raise ValueError('User with given email does not exist')

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.

        Args:
            email (str): The email of the superuser.
            password (str): The password of the superuser.
            **extra_fields: Extra fields to be saved with the superuser.

        Raises:
            ValueError: If no email or password is provided, or if is_staff or is_superuser is not True.

        Returns:
            User: The superuser that was created.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not password:
            raise ValueError('Superusers must have a password.')

        return self.create_user(email, password=password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    login_token = models.CharField(max_length=255, blank=True, null=True)
    login_token_expiration = models.DateTimeField(null=True, blank=True)


    objects = CustomUserManager()

    def set_password(self, raw_password):
        """
        Override the set_password to handle the possibility of non-superusers
        not having a password.

        Args:
            raw_password (str): The raw password that was entered by the user.

        Returns:
            None
        """
        if self.is_superuser:
            super().set_password(raw_password)
        else:
            self.password = None

    def __str__(self):
        """
        Returns a string representation of the User object.

        Returns:
            str: The email of the user.
        """
        return self.email

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class QuestionType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    choices = JSONField(null=True, blank=True)
    order = models.PositiveIntegerField()
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    
class Invitation(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='invitations')
    email = models.EmailField()
    invitation_link = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f"Invitation for {self.email}"

class ResponseToQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)
    selected_choices = JSONField(null=True, blank=True)

    def __str__(self):
        return f"Response to {self.question.text}"

class Invitation(models.Model):
    """
    A model representing an invitation to take a survey.

    Attributes:
        survey (Survey): The survey that the invitation is for.
        email (str): The email address that the invitation is being sent to.
        code (str): A unique code that identifies the invitation.
        expiration_date (datetime): The date and time when the invitation expires.
        sent_date (datetime): The date and time when the invitation was sent.

    Methods:
        save(*args, **kwargs): Overrides the default save method to generate a unique code if one is not provided.
        __str__(): Returns a string representation of the Invitation object.

    Raises:
        Exception: If a unique code cannot be generated after 100 attempts.

    Returns:
        None
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='invitations')
    email = models.EmailField()
    invitation_link = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to generate a unique code if one is not provided.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            Exception: If a unique code cannot be generated after 100 attempts.

        Returns:
            None
        """
        if not self.invitation_link:
            # Ensure the code is unique
            self.invitation_link = self.generate_unique_code()
            self.expiration_date = get_expiration_date()
            
        super().save(*args, **kwargs)


    def generate_unique_code(self):
        """
        Generates a unique code for the invitation.

        Raises:
            Exception: If a unique code cannot be generated after 100 attempts.

        Returns:
            str: The unique code.
        """
        for _ in range(100):
            new_code = get_random_string(length=20)
            if not Invitation.objects.filter(invitation_link=new_code).exists():
                return new_code
            
        raise Exception("Could not generate a unique invitation_link for the invitation")
    
    def __str__(self):
        """
        Returns a string representation of the Invitation object in the following format:
        'Invitation to {email} for survey {survey title}'

        Returns:
            str: A string representation of the Invitation object.
        """
        return f"Invitation to {self.email} for survey {self.survey.title}"
    