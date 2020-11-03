from django import forms
from dashboard.models import Review

class ReviewForm(ModelForm):
    class Meta:
            model = Review
            fields = ('number', 'game', 'release_date', 'price', 'owners', 'developer', 'publisher', 'average_playtime', 'median_playtime', 'metascore')
            labels = {
                'number': 'Numero',
                'game': 'Jogo',
                'release_date': 'Data de lançamento',
                'price': 'Preço',
                'owners': 'Jogadores',
                'developer': 'Desenvolvedor',
                'publisher': 'Publicador',
                'average_playtime': 'Tempo medio de jogo',
                'median_playtime': 'Tempo mediano de jogo',
                'metascore': 'Metascore',
            }