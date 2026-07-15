const variants = {
  primary: "bg-blue-600 hover:bg-blue-700 text-white",

  secondary: "bg-slate-200 hover:bg-slate-300 text-slate-800",

  danger: "bg-red-600 hover:bg-red-700 text-white",

  outline: "border border-slate-300 bg-white hover:bg-slate-100 text-slate-700",
};

function Button({
  children,
  variant = "primary",
  type = "button",
  className = "",
  disabled = false,
  onClick,
}) {
  return (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      className={`
        w-full
        rounded-lg
        px-4
        py-3
        font-medium
        transition
        duration-200
        disabled:cursor-not-allowed
        disabled:opacity-60
        ${variants[variant]}
        ${className}
      `}
    >
      {children}
    </button>
  );
}

export default Button;
