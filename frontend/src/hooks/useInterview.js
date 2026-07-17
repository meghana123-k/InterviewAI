// path: frontend/src/hooks/useInterview.js

import { useEffect, useState } from "react";

import {
  getCurrentQuestion,
  getProgress,
  submitAnswer as submitInterviewAnswer,
} from "../services/interviewService";

export default function useInterview(interviewId) {
  const [question, setQuestion] = useState(null);
  const [progress, setProgress] = useState(null);

  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  const [completed, setCompleted] = useState(false);

  const loadInterview = async () => {
    try {
      setLoading(true);

      const [questionData, progressData] = await Promise.all([
        getCurrentQuestion(interviewId),
        getProgress(interviewId),
      ]);

      if (questionData.completed) {
        setCompleted(true);
        return;
      }

      setQuestion(questionData);
      setProgress(progressData);
    } catch (error) {
      console.error("Failed to load interview:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmitAnswer = async (answer) => {
    if (!question) return;

    try {
      setSubmitting(true);

      await submitInterviewAnswer(question.id, answer);

      await loadInterview();
    } catch (error) {
      console.error("Failed to submit answer:", error);
      throw error;
    } finally {
      setSubmitting(false);
    }
  };

  useEffect(() => {
    if (interviewId) {
      loadInterview();
    }
  }, [interviewId]);

  return {
    question,
    progress,
    loading,
    submitting,
    completed,
    submitAnswer: handleSubmitAnswer,
    refresh: loadInterview,
  };
}
