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

  return(
  <div className={className}>
      <div>
          <i
              className={field.icon}
              style={{color: 'black', fontSize: '100%'}}
              alt={field.name}
          />
      <span>{field.name} </span>
      </div>
      <div>
          <span>{field.explanation}</span>
      </div>
  </div>);
}

function DraggableSidebarField(props) {
  const { field, ...rest } = props;

  const id = useRef(nanoid());

  const { attributes, listeners, setNodeRef } = useDraggable({
    id: id.current,
    data: {
      field,
      fromSidebar: true
    }
  });

  return (
    <div
      ref={setNodeRef}
      className="sidebar-field"
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
      {fields.map((f) => (
        <DraggableSidebarField key={f.type} field={f} />
      ))}
    </div>
  );
}
