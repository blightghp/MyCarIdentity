import { Car, UserProfile, Recommendation } from '../types';

const API_BASE = 'http://localhost:8000/api'; // TODO: jogar isso pra um .env depois

// helper pra não repetir o trycatch em tudo
async function fetchWrapper<T>(endpoint: string, options?: RequestInit): Promise<T> {
  try {
    const res = await fetch(`${API_BASE}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
      },
      ...options,
    });
    
    if (!res.ok) {
      throw new Error(`deu ruim na api: ${res.status}`);
    }
    
    return await res.json();
  } catch (err) {
    console.error('erro na requisição:', err);
    throw err; // deixa quem chamou tratar
  }
}

export const api = {
  buscarCarros: (filtros?: any) => {
    // TODO: implementar a conversão dos filtros pra query string
    return fetchWrapper<Car[]>('/carros');
  },
  
  buscarCarro: (id: string) => {
    return fetchWrapper<Car>(`/carros/${id}`);
  },
  
  buscarRecomendacao: (perfil: UserProfile) => {
    return fetchWrapper<Recommendation[]>('/recomendar', {
      method: 'POST',
      body: JSON.stringify(perfil),
    });
  },
  
  buscarMarcas: () => {
    return fetchWrapper<string[]>('/marcas');
  },
  
  buscarCategorias: () => {
    return fetchWrapper<string[]>('/categorias');
  }
};
