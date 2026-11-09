Najlepiej zastąpić instrukcje if/else obiektem przechowującym konfiguracje.

Zrefaktoryzowany kod

javascript
const configs = {
  development: {
    apiUrl: 'http://localhost:3000/api',
    debug: true,
    timeout: 5000
  },
  testing: {
    apiUrl: 'http://test-server:3000/api',
    debug: true,
    timeout: 5000
  },
  staging: {
    apiUrl: 'https://staging.example.com/api',
    debug: false,
    timeout: 10000
  },
  production: {
    apiUrl: 'https://api.example.com',
    debug: false,
    timeout: 15000
  }
};

function getEnvironmentConfig(env) {
  return configs[env] || configs.development;
}
Co poprawiono?
Usunięto wiele instrukcji if/else.

Wszystkie konfiguracje znajdują się w jednym miejscu.

Dodanie nowego środowiska jest prostsze.

Kod jest krótszy i bardziej czytelny.

Nieznane środowisko domyślnie korzysta z development.