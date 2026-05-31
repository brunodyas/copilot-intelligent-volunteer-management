from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/b4', tags=['feature'])

@router.get('/status')
def feature_b4_status():
    return {'ok': True, 'feature': 'Integrar IA para alocação de voluntários', 'task': 'B4'}
