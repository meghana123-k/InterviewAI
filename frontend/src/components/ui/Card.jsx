// components/ui/Card.jsx

function Card({ children, className = "" }) {
  return (
    <div
      className={`
        relative
        overflow-hidden
        rounded-3xl
        border
        border-white/20
        bg-white/70
        p-8
        shadow-2xl
        backdrop-blur-xl
        dark:border-slate-700
        dark:bg-slate-900/60
        ${className}
      `}
    >
      {children}
    </div>
  );
}

export default Card;