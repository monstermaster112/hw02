#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF 内容提取脚本
用于从 PDF 文件中提取文本内容
"""

import os

def extract_with_pdfplumber(pdf_path):
    """使用 pdfplumber 提取 PDF 内容"""
    try:
        import pdfplumber
        
        content = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    content.append(text)
        
        return "\n".join(content)
    except ImportError:
        print("pdfplumber 未安装，正在尝试安装...")
        os.system("pip install pdfplumber")
        return extract_with_pdfplumber(pdf_path)
    except Exception as e:
        print(f"pdfplumber 提取失败：{e}")
        return None

def extract_with_pymupdf(pdf_path):
    """使用 PyMuPDF (fitz) 提取 PDF 内容"""
    try:
        import fitz  # PyMuPDF
        
        content = []
        doc = fitz.open(pdf_path)
        for page in doc:
            text = page.get_text()
            if text:
                content.append(text)
        doc.close()
        
        return "\n".join(content)
    except ImportError:
        print("PyMuPDF 未安装，正在尝试安装...")
        os.system("pip install pymupdf")
        return extract_with_pymupdf(pdf_path)
    except Exception as e:
        print(f"PyMuPDF 提取失败：{e}")
        return None

def extract_with_pdfminer(pdf_path):
    """使用 pdfminer.six 提取 PDF 内容"""
    try:
        from pdfminer.high_level import extract_text
        
        text = extract_text(pdf_path)
        return text
    except ImportError:
        print("pdfminer.six 未安装，正在尝试安装...")
        os.system("pip install pdfminer.six")
        return extract_with_pdfminer(pdf_path)
    except Exception as e:
        print(f"pdfminer.six 提取失败：{e}")
        return None

def main():
    # PDF 文件路径
    pdf_path = r"c:\Users\lenovo\Desktop\hw02\基于 STM32 单片机的智能浇花系统设计_彭霞.pdf"
    
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误：文件不存在 - {pdf_path}")
        return
    
    print(f"正在读取文件：{pdf_path}")
    print("-" * 50)
    
    # 尝试使用不同的库提取内容
    content = None
    
    # 方法 1: 使用 pdfplumber (推荐)
    print("尝试使用 pdfplumber 提取...")
    content = extract_with_pdfplumber(pdf_path)
    
    # 方法 2: 如果 pdfplumber 失败，尝试 PyMuPDF
    if content is None or content.strip() == "":
        print("尝试使用 PyMuPDF 提取...")
        content = extract_with_pymupdf(pdf_path)
    
    # 方法 3: 如果 PyMuPDF 失败，尝试 pdfminer
    if content is None or content.strip() == "":
        print("尝试使用 pdfminer.six 提取...")
        content = extract_with_pdfminer(pdf_path)
    
    if content and content.strip():
        print("\n" + "=" * 50)
        print("提取成功！内容如下:")
        print("=" * 50)
        print(content)
        
        # 将内容保存到文本文件
        output_path = pdf_path.replace(".pdf", "_extracted.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n内容已保存到：{output_path}")
    else:
        print("未能提取到内容，请检查 PDF 是否为扫描件（需要 OCR）")

if __name__ == "__main__":
    main()