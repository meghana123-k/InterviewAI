import { createContext, useContext, useEffect, useState } from "react";
import { saveTokens, clearTokens, getAccessToken } from "../utils/token";
import {
  login as loginService,
  register as registerService,
  getCurrentUser,
} from "../services/authService";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const loadUser = async () => {
    try {
      if (!getAccessToken()) {
        setLoading(false);
        return;
      }

      const response = await getCurrentUser();
      setUser(response.data);
    } catch (error) {
      clearTokens();
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadUser();
  }, []);

  const login = async (credentials) => {
    const response = await loginService(credentials);

    saveTokens(response.data);

    await loadUser();
  };

  const register = async (data) => {
    await registerService(data);
  };

  const logout = () => {
    clearTokens();
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        logout,
        register,
        loadUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
