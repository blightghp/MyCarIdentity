export type Personalidade = 'aventureiro' | 'conservador' | 'esportivo' | 'economico' | 'status';
export type Categoria = 'hatch' | 'sedan' | 'suv' | 'pickup' | 'esportivo' | 'luxo';
export type UsoPrincipal = 'cidade' | 'estrada' | 'misto';

export interface Car {
  id: string; // no banco pode ser number, mas aqui a gente usa string
  modelo: string;
  marca: string;
  anoFabricacao: number;
  anoModelo: number;
  precoFipe: number;
  precoMercado: number;
  categoria: Categoria;
  combustivel: string;
  cambio: string;
  manutencaoCustoMensal: number;
  seguroMedioAnual: number;
  consumoCidade: number; // km/l
  consumoEstrada: number; // km/l
  notaSeguranca: number;
  notaConforto: number;
  notaDesempenho: number;
  notaCustoBeneficio: number;
  imagemUrl?: string; // opcional pq às vezes não tem foto
  descricao: string;
}

export interface UserProfile {
  nome: string;
  rendaMensal: number;
  valorEntrada: number;
  parcelasMax: number;
  personalidade: Personalidade;
  prioridades: string[];
  usoPrincipal: UsoPrincipal;
}

export interface Recommendation {
  car: Car;
  score: number; // % de match
  justificativa: string;
  parcelaEstimada: number;
  comprometimentoRendaPct: number;
}
