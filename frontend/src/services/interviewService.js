import api from "./api";

export const createInterview = async (data) => {
  const response = await api.post("/interviews/configure/", data);
  return response.data;
};

export const getInterview = async (id) => {
  const response = await api.get(`/interviews/${id}/`);
  return response.data;
};

export const getCurrentQuestion = async (id) => {
  const response = await api.get(`/interviews/${id}/question/`);
  return response.data;
};

export const submitAnswer = async (questionId, answer) => {
  const response = await api.post(
    `/interviews/question/${questionId}/answer/`,
    {
      answer,
    },
  );

  return response.data;
};
