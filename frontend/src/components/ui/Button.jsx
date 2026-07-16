const variants = {
  primary:
    "bg-gradient-to-r from-violet-600 to-indigo-600 text-white hover:scale-[1.02]",

  secondary: "bg-slate-200 text-slate-800 hover:bg-slate-300",

  danger: "bg-gradient-to-r from-red-500 to-pink-500 text-white",

  outline: "border border-slate-300 bg-white text-slate-700 hover:bg-slate-100",
};

function Button({
  children,
  variant = "primary",
  type = "button",
  disabled = false,
  className = "",
  onClick,
}) {
  return (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      className={`
        w-full
        rounded-xl
        py-3
        font-semibold
        shadow-lg
        transition-all
        duration-300
        disabled:opacity-50
        ${variants[variant]}
        ${className}
      `}
    >
      {children}
    </button>
  );
}

export default Button;
