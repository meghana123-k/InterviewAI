// components/ui/Card.jsx

function Card({ children, className = "" }) {
  return (
    <div
      className={`
        rounded-2xl
        bg-white
        p-8
        shadow-lg
        ${className}
      `}
    >
      {children}
    </div>
  );
}

export default Card;
