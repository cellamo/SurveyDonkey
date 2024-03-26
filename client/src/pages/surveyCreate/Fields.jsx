import { Dropdown } from "primereact/dropdown";
import { Checkbox } from "primereact/checkbox";
import { RadioButton } from "primereact/radiobutton";
import { Rating } from "primereact/rating";
export const fields = [
  {
    type: "multiplechoice",
    icon: "pi pi-check",
    name: "Multiple Choice",
    explanation: "Choose from a list of predefined options.",
  },
  {
    type: "singlechoice",
    icon: "pi pi-check-circle",
    name: "Single Choice",
    explanation: "Can only select one option with radio buttons.",
  },
  {
    type: "checkbox",
    icon: "pi pi-check-square",
    name: "Checkboxes",
    explanation: "Can Select multiple options from a list.",
  },
  {
    type: "dropdown",
    icon: "pi pi-arrow-circle-down",
    name: "Dropdown List",
    explanation: "A single-choice question in the form of a dropdown menu.",
  },
  {
    type: "star",
    icon: "pi pi-star",
    name: "Star Rating",
    explanation: "Lets rate items with stars to express their satisfaction.",
  },
];

export const renderers = {
  multiplechoice: () => (
    <div>
      <span>This is a multiple choice question!</span>
      <div className="flex flex-wrap gap-3">
        <div className="p-col-12 flex">
          <div className="flex align-items-center">
            <RadioButton checked={false} />
            <label className="ml-2">A) 0.0012 grams</label>
          </div>
          <div className="flex align-items-center">
            <RadioButton checked={false} />
            <label className="ml-2">B) 0.00012 grams</label>
          </div>
          <div className="flex align-items-center">
            <RadioButton checked={false} />
            <label className="ml-2">C) 0.000012 grams</label>
          </div>
          <div className="flex align-items-center">
            <RadioButton checked={true} />
            <label className="ml-2">D) Somali</label>
          </div>
        </div>
      </div>
    </div>
  ),

  singlechoice: () => (
    <div>
      <span>This is a single choice question!</span>
      <div className="flex flex-wrap gap-3">
        <div className="p-col-12 flex">
          <div className="flex align-items-center">
            <RadioButton checked={false} />
            <label className="ml-2">No</label>
          </div>
          <div className="flex align-items-center">
            <RadioButton checked={true} />
            <label className="ml-2">Yes</label>
          </div>
        </div>
      </div>
    </div>
  ),

  checkbox: () => (
    <div>
      <span>This is a question with checkdown options!</span>
      <div>
        <div className="flex flex-wrap justify-content-center gap-3">
          <div className="flex align-items-center">
            <Checkbox checked={true} />
            <label className="ml-2">Option 1</label>
          </div>
          <div className="flex align-items-center">
            <Checkbox checked={false} />
            <label className="ml-2">Option 2</label>
          </div>
          <div className="flex align-items-center">
            <Checkbox checked={true} />
            <label className="ml-2">Option 3</label>
          </div>
        </div>
      </div>
    </div>
  ),

  dropdown: () => (
    <div>
      <span>This is a question with a dropdown list!</span>
      <div>
        <Dropdown
          options={["Option 1", "Option 2", "Option 3"]}
          placeholder="Select an answer"
          className="w-full md:w-14rem"
        />
      </div>
    </div>
  ),

  star: () => (
    <div>
      <span>This is a question where you can rate with stars!</span>
      <Rating cancel={false} />
    </div>
  ),
};
