/**
 * Pobiera dane użytkownika z API.
 *
 * @param {number|string} userId - Identyfikator użytkownika.
 * @returns {Promise<Object|null>} Dane użytkownika (name, email, lastLogin)
 * lub null w przypadku błędu.
 *
 * @throws {Error} Błąd odpowiedzi HTTP.
 */
function fetchUserData(userId) {
    return fetch(`https://api.example.com/users/${userId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        return {
          name: data.name,
          email: data.email,
          lastLogin: new Date(data.lastLoginTimestamp)
        };
      })
      .catch(error => {
        console.error('Fetch error:', error);
        return null;
      });
  }