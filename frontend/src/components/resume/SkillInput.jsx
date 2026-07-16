import { useState } from "react";
import { Plus } from "lucide-react";

function SkillInput({ onAdd }) {
  const [value, setValue] = useState("");

  const handleAdd = () => {
    const skill = value.trim();

    if (!skill) return;

    onAdd(skill);
    setValue("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handleAdd();
    }
  };

  return (
    <div className="mt-6">
      <label
        className="
          mb-3
          block
          text-sm
          font-semibold
          text-slate-700
          dark:text-slate-300
        "
      >
        Add New Skill
      </label>

      <div className="flex gap-3">
        <input
          type="text"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="React, Java, Spring Boot, AWS..."
          className="
            flex-1
            rounded-2xl
            border
            border-slate-300
            bg-white/80
            px-4
            py-3
            text-slate-800
            shadow-sm
            backdrop-blur-md
            transition-all
            duration-300
            focus:border-violet-500
            focus:ring-4
            focus:ring-violet-200
            dark:border-slate-700
            dark:bg-slate-800/60
            dark:text-white
            dark:focus:ring-violet-900
          "
        />

        <button
          type="button"
          onClick={handleAdd}
          className="
            flex
            items-center
            gap-2
            rounded-2xl
            bg-gradient-to-r
            from-violet-600
            to-cyan-500
            px-6
            py-3
            font-semibold
            text-white
            shadow-lg
            transition-all
            duration-300
            hover:scale-105
            hover:shadow-xl
            active:scale-95
          "
        >
          <Plus size={18} />
          Add
        </button>
      </div>
    </div>
  );
}

export default SkillInput;
