import json

nb = json.load(open(r'e:\VINAI\Day-11-Guardrails-HITL-Responsible-AI\notebooks\lab11_guardrails_hitl.ipynb', 'r', encoding='utf-8'))

code_idx = 0
for i, c in enumerate(nb['cells']):
    if c['cell_type'] == 'code':
        code_idx += 1
        # Show cells 7-9 (unsafe attack results)
        if code_idx < 7 or code_idx > 9:
            continue
        exec_count = c.get('execution_count', '?')
        outputs = c.get('outputs', [])
        src_first = c['source'][0][:80].strip() if c['source'] else 'empty'
        
        output_text = []
        for out in outputs:
            if out.get('output_type') == 'stream':
                output_text.extend(out.get('text', []))
            elif out.get('output_type') == 'execute_result':
                output_text.extend(out.get('data', {}).get('text/plain', []))
            elif out.get('output_type') == 'error':
                output_text.append(f"ERROR: {out.get('ename','')}: {out.get('evalue','')[:200]}\n")
        
        combined = ''.join(output_text)
        
        print(f"\n{'='*70}")
        print(f"CODE CELL {code_idx} (exec={exec_count}): {src_first}")
        print(f"{'='*70}")
        print(combined[:5000])
        if len(combined) > 5000:
            print(f"... [TRUNCATED, total {len(combined)} chars]")
