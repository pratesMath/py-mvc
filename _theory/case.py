'''
- exc_type:
    - 0 tipo da exceção que ocorreu, se houver.
    - Se não ocorreu nenhuma exceção, este parametro será None.
- exc_val:
    - O valor da exceção que ocorreu, se houver
    - Se não ocorreu nenhuma exceção, este parametro será None.
- exc_tb:
    - O traceback (rastreamento de pilha) associado a exceção que ocorreu
    - Se não ocorreu nenhuma exceção, este parametro será None.
'''
class Something:
    def __enter__(self):
        print('step 1')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('step 3')

with Something() as something:
    print('step 2')
