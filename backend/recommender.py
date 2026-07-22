from models import Car, UserProfile, Recommendation
from typing import List

class CarRecommender:
    def _calcular_parcela(self, valor_financiado: float, parcelas: int, taxa_juros_mensal: float = 0.015) -> float:
        # a gente precisa simular um juros basico senao ninguem paga parcela real
        # usando formula de price aqui na humildade
        if parcelas == 0:
            return 0.0
        if valor_financiado <= 0:
            return 0.0
        fator = (taxa_juros_mensal * (1 + taxa_juros_mensal)**parcelas) / (((1 + taxa_juros_mensal)**parcelas) - 1)
        return valor_financiado * fator

    def calcular_score(self, car: Car, user: UserProfile) -> float:
        score = 0.0
        
        # prioridades (pesos pesados)
        for p in user.prioridades:
            if p == 'seguranca':
                score += car.nota_seguranca * 2
            elif p == 'economia':
                score += car.nota_custo_beneficio * 2
                # da uns pontinhos extras se beber pouco
                if car.consumo_cidade > 12: score += 1
            elif p == 'conforto':
                score += car.nota_conforto * 2
            elif p == 'desempenho':
                score += car.nota_desempenho * 2
            elif p == 'estetica':
                # meio subjetivo, mas vamos dar um peso pra certas categorias
                if car.categoria in ['esportivo', 'suv', 'luxo']:
                    score += 3
                    
        # match de uso principal
        if user.uso_principal == 'cidade':
            if car.categoria in ['hatch', 'sedan compact']: score += 2
            if car.consumo_cidade >= 11: score += 1
        elif user.uso_principal == 'estrada':
            if car.categoria in ['sedan', 'suv']: score += 2
            if car.nota_desempenho >= 4: score += 1
        elif user.uso_principal == 'misto':
            score += 1 # qualquer um serve kkk
            
        # match de personalidade
        # TODO: afinar isso dps, ta meio engessado
        if user.personalidade == 'aventureiro' and car.categoria in ['pickup', 'suv']:
            score += 3
        elif user.personalidade == 'conservador' and car.marca in ['Toyota', 'Honda']:
            score += 3
        elif user.personalidade == 'esportivo' and (car.categoria == 'esportivo' or car.nota_desempenho == 5):
            score += 3
        elif user.personalidade == 'economico' and car.nota_custo_beneficio >= 4:
            score += 3
        elif user.personalidade == 'status' and car.categoria in ['luxo', 'suv']:
            score += 3

        return score

    def filtrar_por_renda(self, carros: List[Car], renda: float, entrada: float, parcelas: int) -> List[dict]:
        carros_viaveis = []
        limite_parcela = renda * 0.30 # ninguem quer o nome no serasa, max 30% da renda

        for car in carros:
            valor_financiado = car.preco_mercado - entrada
            # se a entrada for maior q o carro, show
            if valor_financiado <= 0:
                carros_viaveis.append({'car': car, 'parcela': 0.0, 'pct_renda': 0.0})
                continue
                
            parcela_estimada = self._calcular_parcela(valor_financiado, parcelas)
            if parcela_estimada <= limite_parcela:
                pct_renda = (parcela_estimada / renda) * 100
                carros_viaveis.append({'car': car, 'parcela': parcela_estimada, 'pct_renda': pct_renda})
                
        return carros_viaveis

    def recomendar(self, user: UserProfile, carros: List[Car], top_n: int = 5) -> List[Recommendation]:
        # tira os carros que o cara nao consegue pagar
        viaveis = self.filtrar_por_renda(carros, user.renda_mensal, user.valor_entrada, user.parcelas_max)
        
        recomendacoes = []
        for item in viaveis:
            c = item['car']
            score = self.calcular_score(c, user)
            
            # TODO: gerar um texto melhor, quem sabe jogar pro gpt depois rsrs
            justi = f"Esse carro bateu uma pontuação legal com seu perfil {user.personalidade}."
            if item['parcela'] == 0:
                justi += " E você compra à vista!"
                
            recomendacoes.append(Recommendation(
                car=c,
                score=score,
                justificativa=justi,
                parcela_estimada=item['parcela'],
                comprometimento_renda_pct=item['pct_renda']
            ))
            
        # ordena do maior score pro menor
        recomendacoes.sort(key=lambda x: x.score, reverse=True)
        return recomendacoes[:top_n]
