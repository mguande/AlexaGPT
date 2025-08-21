#!/usr/bin/env python3
"""
Script para criar ícones simples para a Alexa Skill
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    """Cria um ícone simples"""
    # Cria uma imagem com fundo azul
    img = Image.new('RGB', (size, size), color='#0078D4')
    draw = ImageDraw.Draw(img)
    
    # Adiciona texto "AG" (AlexaGPT)
    try:
        # Tenta usar uma fonte do sistema
        font_size = size // 3
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback para fonte padrão
        font = ImageFont.load_default()
    
    text = "AG"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Desenha o texto em branco
    draw.text((x, y), text, fill='white', font=font)
    
    # Salva a imagem
    img.save(filename)
    print(f"✅ Ícone criado: {filename} ({size}x{size})")

def main():
    """Função principal"""
    print("🎨 Criando ícones para AlexaGPT...")
    
    # Cria diretório para ícones se não existir
    if not os.path.exists('icons'):
        os.makedirs('icons')
    
    # Cria ícones nos tamanhos necessários
    create_icon(108, 'icons/small_icon.png')  # 108x108
    create_icon(512, 'icons/large_icon.png')  # 512x512
    
    print("\n📋 Instruções para usar os ícones:")
    print("1. Vá em 'Distribution' > 'Skill Preview'")
    print("2. Em 'Portuguese (Brazil)', clique em 'Edit'")
    print("3. Faça upload dos ícones:")
    print("   - Small Icon: icons/small_icon.png")
    print("   - Large Icon: icons/large_icon.png")
    print("4. Clique em 'Save'")

if __name__ == "__main__":
    main()
