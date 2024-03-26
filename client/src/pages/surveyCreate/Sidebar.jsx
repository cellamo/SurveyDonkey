import { useDraggable } from "@dnd-kit/core";
import { nanoid } from "nanoid";
import React, { useRef } from "react";

import { fields } from "./Fields.jsx";

export function SidebarField(props) {
  const { field, overlay } = props;

  let className = "sidebar-field";
  if (overlay) {
    className += " overlay";
  }

  return (
    <div className={className}>
      <i className={`${field.icon} sidebar-field-icon`} alt={field.name} />
      <div className="sidebar-field-info">
        <span className="sidebar-field-name">{field.name} </span>
        <span className="sidebar-field-explanation">{field.explanation}</span>
      </div>
    </div>
  );
}

function DraggableSidebarField(props) {
  const { field, ...rest } = props;

  const id = useRef(nanoid());

  const { attributes, listeners, setNodeRef } = useDraggable({
    id: id.current,
    data: {
      field,
      fromSidebar: true,
    },
  });

  return (
    <div
      ref={setNodeRef}
      className="sidebar-field-container"
      {...listeners}
      {...attributes}
    >
      <SidebarField field={field} {...rest} />
    </div>
  );
}

export default function Sidebar(props) {
  const { fieldsRegKey } = props;

  return (
    <div key={fieldsRegKey} className="survey-create-sidebar">
      <div id="survey-create-sidebar-user-email">
        <p>b21627304@cs.hacettepe.edu.tr</p>
      </div>
      {fields.map((f) => (
        <DraggableSidebarField key={f.type} field={f} />
      ))}
    </div>
  );
}
