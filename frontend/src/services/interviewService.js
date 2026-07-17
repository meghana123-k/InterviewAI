import api from "./api";

// Create Interview
export const createInterview = async (data) => {
  const response = await api.post("/interviews/configure/", data);
  return response.data;
};

// Interview Details
export const getInterview = async (id) => {
  const response = await api.get(`/interviews/${id}/`);
  return response.data;
};

// Current Question
export const getCurrentQuestion = async (id) => {
  const response = await api.get(`/interviews/${id}/question/`);
  return response.data;
};

// Submit Answer
export const submitAnswer = async (questionId, answer) => {
  const response = await api.post(
    `/interviews/question/${questionId}/answer/`,
    {
      answer,
    },
  );

  return response.data;
};

// Progress
export const getProgress = async (id) => {
  const response = await api.get(`/interviews/${id}/progress/`);
  return response.data;
};
