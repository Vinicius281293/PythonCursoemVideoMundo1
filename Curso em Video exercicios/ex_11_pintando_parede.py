# Curso em vídeo
# Aula 11
# Pintando Parede

largura = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = largura * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, alt, area))
tinta = area / 2
print('Para pintar a parede, você precisará de {}l de tinta.'.format(tinta))
