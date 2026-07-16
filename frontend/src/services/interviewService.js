import api from "./api";

export const createInterview = async (data) => {
  const response = await api.post("/interviews/configure/", data);
  return response.data;
};
