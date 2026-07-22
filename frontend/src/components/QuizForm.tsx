import React, { useState } from 'react';
import { UserProfile, Personalidade, UsoPrincipal } from '../types';
import { api } from '../services/api';

// TODO: refatorar isso aqui, separar em componentes menores depois
export const QuizForm = () => {
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [profile, setProfile] = useState<Partial<UserProfile>>({
    prioridades: []
  });

  // TODO: adicionar validação dos campos antes de avançar
  const nextStep = () => setStep(s => Math.min(s + 1, 5));
  const prevStep = () => setStep(s => Math.max(s - 1, 1));

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setProfile(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      // gambiarrinha mas funciona pra forçar o tipo enquanto não tem validação forte
      const res = await api.buscarRecomendacao(profile as UserProfile);
      console.log('recomendações chegaram:', res);
      // TODO: passar isso pro estado global ou pro pai pra mostrar os resultados
    } catch (err) {
      alert('vixe, deu erro ao buscar as recomendações');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="quiz-container">
      <div className="progress-bar" style={{ width: `${(step / 5) * 100}%` }}></div>
      
      <form onSubmit={step === 5 ? handleSubmit : (e) => { e.preventDefault(); nextStep(); }}>
        {step === 1 && (
          <div className="step-content">
            <h2>Dados Pessoais</h2>
            <label>Qual seu nome?</label>
            <input name="nome" value={profile.nome || ''} onChange={handleChange} required />
          </div>
        )}
        
        {step === 2 && (
          <div className="step-content">
            <h2>Financeiro</h2>
            <label>Renda Mensal (R$)</label>
            <input type="number" name="rendaMensal" value={profile.rendaMensal || ''} onChange={handleChange} required />
            <label>Valor de Entrada (R$)</label>
            <input type="number" name="valorEntrada" value={profile.valorEntrada || ''} onChange={handleChange} required />
            <label>Máximo de parcelas</label>
            <input type="number" name="parcelasMax" value={profile.parcelasMax || ''} onChange={handleChange} required />
          </div>
        )}

        {step === 3 && (
          <div className="step-content">
            <h2>Personalidade</h2>
            <label>Como vc se define no trânsito?</label>
            <select name="personalidade" value={profile.personalidade || ''} onChange={handleChange} required>
              <option value="">Selecione...</option>
              <option value="aventureiro">Aventureiro (mato e lama)</option>
              <option value="conservador">Conservador (só quer chegar em paz)</option>
              <option value="esportivo">Esportivo (pé pesado)</option>
              <option value="economico">Econômico (conta cada gota)</option>
              <option value="status">Status (gosta de chamar atenção)</option>
            </select>
          </div>
        )}

        {/* passo 4 (prioridades) simplificado por enquanto */}
        {step === 4 && (
          <div className="step-content">
            <h2>Prioridades</h2>
            <p>Depois a gente bota os checkboxes bonitinhos, por enquanto deixa assim msm</p>
            {/* TODO: trocar por checkbox */}
            <input name="prioridades" placeholder="ex: consumo, espaco" onChange={handleChange} />
          </div>
        )}

        {step === 5 && (
          <div className="step-content">
            <h2>Uso Principal</h2>
            <select name="usoPrincipal" value={profile.usoPrincipal || ''} onChange={handleChange} required>
              <option value="">Selecione...</option>
              <option value="cidade">Cidade (trânsito maldito)</option>
              <option value="estrada">Estrada (viagens)</option>
              <option value="misto">Misto (um pouco de cada)</option>
            </select>
          </div>
        )}

        <div className="actions">
          {step > 1 && <button type="button" onClick={prevStep}>Voltar</button>}
          {step < 5 ? (
            <button type="submit">Próximo</button>
          ) : (
            <button type="submit" disabled={loading}>
              {loading ? 'Calculando...' : 'Ver Meu Carro Ideal'}
            </button>
          )}
        </div>
      </form>
    </div>
  );
};
