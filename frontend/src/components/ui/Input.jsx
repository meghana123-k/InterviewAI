function Input({ label, type = "text", placeholder, value, onChange, name }) {
  return (
    <div className="space-y-2">
      <label
        className="
          text-sm
          font-medium
          text-slate-700
          dark:text-slate-300
        "
      >
        {label}
      </label>

      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        name={name}
        className="
          w-full
          rounded-xl
          border
          border-slate-300
          bg-white/80
          px-4
          py-3
          text-slate-800
          backdrop-blur-md
          transition-all
          duration-300
          focus:border-violet-500
          focus:ring-4
          focus:ring-violet-300
          dark:border-slate-700
          dark:bg-slate-800/60
          dark:text-white
        "
      />
    </div>
  );
}

export default Input;
