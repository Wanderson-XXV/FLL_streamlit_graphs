import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Gráfico de Precisão FLL - Fênix Robots",
    page_icon="🤖",
    layout="wide"
)

# CSS customizado para tema escuro
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
    }
    .stMetric {
        background-color: #2d2d2d;
        padding: 15px;
        border-radius: 8px;
    }
    h1, h2, h3, h4, h5, h6, p, span, div {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 style='text-align: center; color: #ff3333;'>🤖 Fênix Robots - Gráfico de Precisão FLL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #cccccc;'>Análise de Precisão de Todas as Rotas</p>", unsafe_allow_html=True)
st.markdown("---")

# Dados da tabela (corrigindo o valor errado de 9000% para 100%)
rota_data = {
    'Round': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15'],
    'Rota 1': [100.0, 60.0, 70.0, 60.0, 80.0, 100.0, 70.0, 70.0, 70.0, 80.0, 100.0, 100.0, 60.0, 70.0, 100.0],
    'Rota 2': [80.0, 100.0, 40.0, 70.0, 85.0, 100.0, 90.0, 85.0, 90.0, 95.0, 100.0, 100.0, 70.0, 80.0, 100.0],
    'Rota 3': [100.0, 80.0, 100.0, 80.0, 100.0, 100.0, 85.0, 80.0, 95.0, 90.0, 100.0, 85.0, 55.0, 70.0, 100.0],
    'Rota 4': [100.0, 100.0, 30.0, 100.0, 100.0, 100.0, 100.0, 100.0, 30.0, 70.0, 85.0, 90.0, 30.0, 60.0, 100.0],
    'Rota 5': [70.0, 60.0, 30.0, 20.0, 75.0, 100.0, 60.0, 75.0, 85.0, 95.0, 80.0, 90.0, 65.0, 90.0, 100.0],
    'Rota 6': [90.0, 90.0, 50.0, 20.0, 90.0, 100.0, 100.0, 100.0, 95.0, 100.0, 80.0, 95.0, 80.0, 70.0, 100.0],
    'Rota 7': [100.0, 90.0, 60.0, 60.0, 90.0, 100.0, 95.0, 90.0, 90.0, 100.0, 100.0, 95.0, 75.0, 88.0, 100.0]
}

df = pd.DataFrame(rota_data)

# Meta de precisão
META = 70.0

# Criar número de índice para o eixo x
df['Indice'] = range(1, len(df) + 1)

# Cores para cada rota
cores_rotas = {
    'Rota 1': '#d4a574',
    'Rota 2': '#b8894e',
    'Rota 3': '#8b6f47',
    'Rota 4': '#c98d5a',
    'Rota 5': '#a67c52',
    'Rota 6': '#9b7653',
    'Rota 7': '#7d5e3f'
}

# Função para criar gráfico de dispersão
def criar_grafico_dispersao(rota_col, cor, titulo):
    fig = go.Figure()
    
    # Adicionar pontos de dispersão
    fig.add_trace(go.Scatter(
        x=df['Indice'],
        y=df[rota_col],
        mode='markers',
        name=titulo,
        marker=dict(
            size=12,
            color=cor,
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>%{text}</b><br>Precisão: %{y:.1f}%<extra></extra>',
        text=df['Round']
    ))
    
    # Adicionar linha de meta
    x_min = 0.5
    x_max = 15.5
    
    fig.add_trace(go.Scatter(
        x=[x_min, x_max],
        y=[META, META],
        mode='lines',
        name=f'Meta: {META}%',
        line=dict(color='#ff3333', width=3, dash='dash'),
        hovertemplate=f'Meta: {META}%<extra></extra>'
    ))
    
    fig.update_layout(
        title=titulo,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#ffffff', size=11),
        height=350,
        xaxis=dict(
            showgrid=False,
            showline=True,
            linewidth=1,
            linecolor='#3a3a3a',
            zeroline=False,
            color='#ffffff',
            title='Índice do Ponto',
            range=[x_min, x_max]
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='#3a3a3a',
            showline=True,
            linewidth=1,
            linecolor='#3a3a3a',
            zeroline=False,
            color='#ffffff',
            title='Precisão (%)',
            range=[0, 105]
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=10)
        ),
        hovermode='closest',
        margin=dict(t=50, b=35, l=50, r=30)
    )
    
    return fig

# Função para criar gráfico geral com todas as rotas
def criar_grafico_geral():
    fig = go.Figure()
    
    simbolos = ['circle', 'square', 'diamond', 'cross', 'x', 'triangle-up', 'star']
    
    for idx, (rota, cor) in enumerate(cores_rotas.items()):
        fig.add_trace(go.Scatter(
            x=df['Indice'],
            y=df[rota],
            mode='markers',
            name=rota,
            marker=dict(
                size=11,
                color=cor,
                line=dict(width=2, color='white'),
                symbol=simbolos[idx]
            ),
            hovertemplate='<b>%{text}</b><br>' + rota + ': %{y:.1f}%<extra></extra>',
            text=df['Round']
        ))
    
    # Linha de meta
    fig.add_trace(go.Scatter(
        x=[0.5, 15.5],
        y=[META, META],
        mode='lines',
        name=f'Meta: {META}%',
        line=dict(color='#ff3333', width=3, dash='dash'),
        hovertemplate=f'Meta: {META}%<extra></extra>'
    ))
    
    fig.update_layout(
        title='Precisão Geral - Comparação de Todas as Rotas',
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#ffffff', size=12),
        height=500,
        xaxis=dict(
            showgrid=False,
            showline=True,
            linewidth=1,
            linecolor='#3a3a3a',
            zeroline=False,
            color='#ffffff',
            title='Índice do Ponto',
            range=[0.5, 15.5]
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='#3a3a3a',
            showline=True,
            linewidth=1,
            linecolor='#3a3a3a',
            zeroline=False,
            color='#ffffff',
            title='Precisão (%)',
            range=[0, 105]
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.18,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=11)
        ),
        hovermode='closest',
        margin=dict(t=100, b=40, l=60, r=40)
    )
    
    return fig

# Gráfico Geral
st.markdown("### 🎯 Gráfico Geral de Precisão")
fig_geral = criar_grafico_geral()
st.plotly_chart(fig_geral, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Gráficos individuais
st.markdown("### 📊 Gráficos Individuais por Rota")

# Primeira linha - Rotas 1, 2, 3
col1, col2, col3 = st.columns(3)

with col1:
    fig1 = criar_grafico_dispersao('Rota 1', cores_rotas['Rota 1'], 'Precisão - Rota 1')
    st.plotly_chart(fig1, use_container_width=True)
    acima_meta = len(df[df['Rota 1'] >= META])
    st.info(f'Pontos acima da meta: {acima_meta}/15')

with col2:
    fig2 = criar_grafico_dispersao('Rota 2', cores_rotas['Rota 2'], 'Precisão - Rota 2')
    st.plotly_chart(fig2, use_container_width=True)
    acima_meta = len(df[df['Rota 2'] >= META])
    st.info(f'Pontos acima da meta: {acima_meta}/15')

with col3:
    fig3 = criar_grafico_dispersao('Rota 3', cores_rotas['Rota 3'], 'Precisão - Rota 3')
    st.plotly_chart(fig3, use_container_width=True)
    acima_meta = len(df[df['Rota 3'] >= META])
    st.info(f'Pontos acima da meta: {acima_meta}/15')

st.markdown("<br>", unsafe_allow_html=True)

# Segunda linha - Rotas 4, 5, 6
col4, col5, col6 = st.columns(3)

with col4:
    fig4 = criar_grafico_dispersao('Rota 4', cores_rotas['Rota 4'], 'Precisão - Rota 4')
    st.plotly_chart(fig4, use_container_width=True)
    acima_meta = len(df[df['Rota 4'] >= META])
    st.info(f'Pontos acima da meta: {acima_meta}/15')

with col5:
    fig5 = criar_grafico_dispersao('Rota 5', cores_rotas['Rota 5'], 'Precisão - Rota 5')
    st.plotly_chart(fig5, use_container_width=True)
    acima_meta = len(df[df['Rota 5'] >= META])
    st.info(f'Pontos acima da meta: {acima_meta}/15')

with col6:
    fig6 = criar_grafico_dispersao('Rota 6', cores_rotas['Rota 6'], 'Precisão - Rota 6')
    st.plotly_chart(fig6, use_container_width=True)
    acima_meta = len(df[df['Rota 6'] >= META])
    st.info(f'Pontos acima da meta: {acima_meta}/15')

st.markdown("<br>", unsafe_allow_html=True)

# Terceira linha - Rota 7 centralizada
col_empty1, col7, col_empty2 = st.columns([1, 1, 1])

with col7:
    fig7 = criar_grafico_dispersao('Rota 7', cores_rotas['Rota 7'], 'Precisão - Rota 7')
    st.plotly_chart(fig7, use_container_width=True)
    acima_meta = len(df[df['Rota 7'] >= META])
    st.info(f'Pontos acima da meta: {acima_meta}/15')

st.markdown("<br><br>", unsafe_allow_html=True)

# Estatísticas Resumidas
st.markdown("### 📈 Estatísticas Resumidas de Todas as Rotas")

# Calcular estatísticas para todas as rotas
stats = []
for rota in ['Rota 1', 'Rota 2', 'Rota 3', 'Rota 4', 'Rota 5', 'Rota 6', 'Rota 7']:
    dados = df[rota]
    stats.append({
        'Rota': rota,
        'Média': round(dados.mean(), 2),
        'Mínima': round(dados.min(), 2),
        'Máxima': round(dados.max(), 2),
        'Acima da Meta': len(dados[dados >= META])
    })

stats_df = pd.DataFrame(stats)

# Encontrar melhor rota
melhor_idx = stats_df['Média'].idxmax()
melhor_rota = stats_df.loc[melhor_idx, 'Rota']
melhor_media = stats_df.loc[melhor_idx, 'Média']

# Exibir cards
cols = st.columns(4)

for idx in range(7):
    with cols[idx % 4]:
        rota_info = stats_df.iloc[idx]
        cor = cores_rotas[rota_info['Rota']]
        
        destaque = "border: 3px solid #ffd700;" if rota_info['Rota'] == melhor_rota else ""
        
        st.markdown(f"""
        <div style='background-color: #2d2d2d; padding: 15px; border-radius: 10px; border-left: 5px solid {cor}; {destaque}'>
            <h4 style='color: {cor}; margin-bottom: 10px; font-size: 16px;'>{rota_info['Rota']}</h4>
            <p style='font-size: 24px; font-weight: bold; color: #ffffff; margin: 5px 0;'>{rota_info['Média']}%</p>
            <p style='color: #aaaaaa; font-size: 12px;'>Média de Precisão</p>
            <hr style='border-color: #3a3a3a; margin: 10px 0;'>
            <p style='color: #cccccc; font-size: 12px;'>Mín: {rota_info['Mínima']}% | Máx: {rota_info['Máxima']}%</p>
            <p style='color: #51cf66; font-size: 12px;'>✓ {rota_info['Acima da Meta']}/15 acima da meta</p>
        </div>
        """, unsafe_allow_html=True)
    
    if idx == 3:
        st.write("")

st.markdown("<br>", unsafe_allow_html=True)

# Melhor Rota em destaque
st.markdown(f"""
<div style='background-color: #2d2d2d; padding: 25px; border-radius: 10px; border: 3px solid #ffd700; text-align: center;'>
    <p style='color: #aaaaaa; font-size: 16px; margin-bottom: 10px;'>🏆 MELHOR DESEMPENHO</p>
    <p style='color: {cores_rotas[melhor_rota]}; font-size: 32px; font-weight: bold; margin: 10px 0;'>{melhor_rota}</p>
    <p style='font-size: 40px; font-weight: bold; color: #ffd700; margin: 15px 0;'>{melhor_media}%</p>
    <p style='color: #cccccc; font-size: 16px;'>Precisão Média</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Tabela de dados
st.markdown("### 📋 Dados Detalhados")
with st.expander("Clique para ver a tabela completa"):
    df_display = df[['Round', 'Rota 1', 'Rota 2', 'Rota 3', 'Rota 4', 'Rota 5', 'Rota 6', 'Rota 7']].copy()
    for col in ['Rota 1', 'Rota 2', 'Rota 3', 'Rota 4', 'Rota 5', 'Rota 6', 'Rota 7']:
        df_display[col] = df_display[col].apply(lambda x: f"{x:.1f}%")
    
    st.dataframe(df_display, use_container_width=True, height=500)

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666666;'>Fênix Robots © 2024 - Gráfico de Precisão FLL</p>", unsafe_allow_html=True)
