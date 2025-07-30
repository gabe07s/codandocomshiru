from fpdf import FPDF

def gerar_pdf_relatorio(tipo, salario, meses_trabalhados, dias_trabalhados, horas_extras, fgts_total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Relatório - Cálculos Trabalhistas", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Tipo: {'CLT Comum' if tipo == '1' else 'Jovem Aprendiz'}", ln=True)
    pdf.cell(200, 10, txt=f"Salário: R$ {salario:.2f}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt="Resultados:", ln=True)
    pdf.cell(200, 10, txt=f"- Décimo terceiro: R$ {calcular_decimo_terceiro(salario, meses_trabalhados):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- FGTS do mês: R$ {calcular_fgts_mensal(salario, tipo):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Multa FGTS: R$ {calcular_multa_fgts(fgts_total):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Férias + 1/3: R$ {calcular_ferias(salario):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Férias proporcionais: R$ {calcular_ferias_proporcionais(salario, meses_trabalhados):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Horas extras: R$ {calcular_hora_extra(salario, horas_extras):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Salário líquido: R$ {calcular_salario_liquido(salario):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Abono PIS: R$ {calcular_abono_pis(salario, meses_trabalhados):.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Rescisão total estimada: R$ {calcular_rescisao(salario, dias_trabalhados, meses_trabalhados, fgts_total):.2f}", ln=True)

    pdf.output("relatorio_calculos.pdf")
    print("PDF gerado com sucesso: relatorio_calculos.pdf")
