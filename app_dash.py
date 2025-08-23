import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Dummy function for demonstration; replace with your actual function
def ask_google_ai(user_input):
    return f"Echo: {user_input}"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    # Fixed header
    html.Div([
        html.H1("JANGIR AI CHATBOT", style={'margin-bottom': '0', 'color': '#f2e9e4'}),
        html.P("Your AI assistant, powered by Google", style={'color': '#c9ada7', 'margin-top': '0'}),
    ], style={
        'position': 'fixed', 'top': '2rem', 'left': '50%', 'transform': 'translateX(-50%)',
        'width': '95vw', 'maxWidth': '700px', 'background': '#22223b', 'zIndex': 100,
        'padding': '36px 24px 24px 24px', 'boxShadow': '0 4px 24px rgba(0,0,0,0.12)',
        'border': '2px solid #4a4e69', 'borderRadius': '18px', 'textAlign': 'center',
        'color': '#fff', 'overflowWrap': 'break-word', 'wordBreak': 'break-word'
    }),

    # Main content
    html.Div([
        dcc.Store(id='chat-history', data=[]),
        html.Div(id='chat-messages', style={
            'height': '250px', 'overflowY': 'auto', 'marginBottom': '1rem',
            'marginTop': '170px', 'paddingRight': '10px'
        }),
        dbc.InputGroup([
            dbc.Input(id='user-input', placeholder='Type your message...', type='text', autoFocus=True),
            dbc.Button('Send', id='send-btn', n_clicks=0, color='primary')
        ], style={'maxWidth': '700px', 'margin': '0 auto'})
    ], style={'maxWidth': '700px', 'margin': '0 auto'})
])

@app.callback(
    Output('chat-messages', 'children'),
    Output('chat-history', 'data'),
    Input('send-btn', 'n_clicks'),
    State('user-input', 'value'),
    State('chat-history', 'data'),
    prevent_initial_call=True
)
def update_chat(n_clicks, user_input, history):
    if not user_input or not user_input.strip():
        return dash.no_update, history
    history = history or []
    history.append({'role': 'user', 'message': user_input})
    bot_response = ask_google_ai(user_input)
    history.append({'role': 'assistant', 'message': bot_response})
    messages = []
    for chat in history:
        if chat['role'] == 'user':
            messages.append(html.Div([
                html.Span("🧑", style={'marginRight': '8px'}),
                html.Span(chat['message'])
            ], style={'textAlign': 'right', 'margin': '8px 0', 'color': '#22223b', 'background': '#f2e9e4', 'borderRadius': '8px', 'padding': '8px 12px', 'display': 'inline-block'}))
        else:
            messages.append(html.Div([
                html.Span("🤖", style={'marginRight': '8px'}),
                html.Span(chat['message'])
            ], style={'textAlign': 'left', 'margin': '8px 0', 'color': '#fff', 'background': '#4a4e69', 'borderRadius': '8px', 'padding': '8px 12px', 'display': 'inline-block'}))
    return messages, history

if __name__ == '__main__':
    app.run(debug=True)