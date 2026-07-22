import React from 'react';
import { Car } from '../types';

interface CarCardProps {
  car: Car;
  showScore?: boolean;
  score?: number;
}

export const CarCard: React.FC<CarCardProps> = ({ car, showScore, score }) => {
  return (
    <div className="car-card">
      {/* TODO: botar uma imagem fallback se o carro n tiver */}
      {car.imagemUrl ? (
        <img src={car.imagemUrl} alt={car.modelo} className="car-image" />
      ) : (
        <div className="car-image-placeholder">Sem foto :(</div>
      )}
      
      <div className="car-info">
        <h3>{car.marca} {car.modelo}</h3>
        <p className="car-price">
          R$ {car.precoMercado.toLocaleString('pt-BR')}
        </p>
        
        <div className="badges">
          <span className="badge category">{car.categoria}</span>
          <span className="badge year">{car.anoModelo}</span>
        </div>

        {/* só mostra os stats básicos por enquanto pra n poluir */}
        <div className="car-stats">
          <span>Segurança: {car.notaSeguranca}/10</span>
          <span>Custo-Benefício: {car.notaCustoBeneficio}/10</span>
        </div>
      </div>
      
      {showScore && score && (
        <div className="match-score">
          {Math.round(score)}% Match
        </div>
      )}
    </div>
  );
};
