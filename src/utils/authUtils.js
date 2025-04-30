import { jwtDecode } from 'jwt-decode';

export function getUserIdFromToken() {
  const token = localStorage.getItem('token');
  if (!token) return null;

  try {
    const decoded = jwtDecode(token);
    return decoded.user_id || decoded.sub || null;
  } catch (e) {
    console.error('Invalid token:', e);
    return null;
  }
}
