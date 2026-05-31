from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/b3', tags=['feature'])

@router.get('/status')
def feature_b3_status():
    return {'ok': True, 'feature': 'Implementar funcionalidades básicas de gestão de voluntários', 'task': 'B3'}
