import { X } from "lucide-react";

function SkillChip({ skill, onRemove }) {
  return (
    <div
      className="
        group
        flex
        items-center
        gap-2
        rounded-full
        border
        border-violet-200
        bg-gradient-to-r
        from-violet-100
        to-cyan-100
        px-4
        py-2
        text-sm
        font-medium
        text-slate-800
        transition-all
        duration-300
        hover:scale-105
        hover:shadow-lg
        dark:border-violet-800
        dark:from-violet-900/40
        dark:to-cyan-900/40
        dark:text-slate-200
      "
    >
      <span>{skill}</span>

      {onRemove && (
        <button
          type="button"
          onClick={() => onRemove(skill)}
          className="
            rounded-full
            p-1
            text-slate-500
            transition
            hover:bg-red-500
            hover:text-white
          "
        >
          <X size={14} />
        </button>
      )}
    </div>
  );
}

export default SkillChip;
