export const saveTokens = (tokens) => {
  localStorage.setItem("access", tokens.access);
  localStorage.setItem("refresh", tokens.refresh);
};

export const removeTokens = () => {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
};

export const getAccessToken = () => localStorage.getItem("access");
