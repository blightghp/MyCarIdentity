import React from 'react';
import { Recommendation } from '../types';
import { CarCard } from './CarCard';

interface ResultPanelProps {
  recommendations: Recommendation[];
}

export const ResultPanel: React.FC<ResultPanelProps> = ({ recommendations }) => {
  if (!recommendations || recommendations.length === 0) {
    return <p>nenhuma recomendação ainda, faz o quiz aí primeiro.</p>;
  }

  // corzinha marota dependendo de quanto pesa no bolso do cara
  const getColorForCommitment = (pct: number) => {
    if (pct < 30) return 'green';
    if (pct < 50) return 'yellow';
    return 'red';
  };

  return (
    <div className="result-panel">
      <h2>Top Carros pra Você</h2>
      
      <div className="recommendations-list">
        {recommendations.map((rec, idx) => (
          <div key={rec.car.id} className="recommendation-item">
            {/* destaque pro primeiro lugar */}
            {idx === 0 && <span className="trophy">🏆 Escolha Ideal</span>}
            
            <CarCard 
              car={rec.car} 
              showScore={true} 
              score={rec.score} 
            />
            
            <div className="recommendation-details">
              <p className="justificativa">{rec.justificativa}</p>
              
              <div className="financeiro-info">
                <span>Parcela: R$ {rec.parcelaEstimada.toFixed(2)}</span>
                <span style={{ color: getColorForCommitment(rec.comprometimentoRendaPct) }}>
                  Compromete {rec.comprometimentoRendaPct.toFixed(1)}% da renda
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
