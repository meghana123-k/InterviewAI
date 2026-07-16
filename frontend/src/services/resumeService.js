import api from "./api";

export const uploadResume = async (formData) => {
  const response = await api.post("/resumes/upload/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export const getLatestResume = async () => {
  const response = await api.get("/resumes/latest/");
  return response.data;
};

export const updateResume = async (data) => {
  const response = await api.patch("/resumes/latest/", data);
  return response.data;
};