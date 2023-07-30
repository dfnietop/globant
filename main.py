from io import BytesIO
import uvicorn as uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
import pandas as pd

from app.globant.global_facade.deparment_facade import DepartmentFacade
from app.globant.global_facade.employed_facade import EmployedFacade
from app.globant.global_facade.job_facade import JobFacade
from app.globant.global_core import schema, model
from app.globant.global_utils.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/files/upload_hired_employees")
def upload_hired_employees_file(file: UploadFile = File(...), db=Depends(db)):
    try:
        # if file.content_type == 'application/csv':
        print('entra')
        contents = file.file.read()
        buffer = BytesIO(contents)
        df = pd.read_csv(buffer, header=None)
        df = df.rename(columns={0: "id", 1: 'name', 2: 'datetime', 3: 'department_id', 4: 'job_id'})
        df.dropna(inplace=True)
        df['job_id'] = df['job_id'].astype(int)
        df['department_id'] = df['department_id'].astype(int)
        buffer.close()
        file.file.close()
        print(df.to_dict(orient='records'))
        employe = EmployedFacade(db, 'hired_employees')
        employe.insert_employe(df.to_dict(orient='records'))
        return {"Response": 200}
    # else:
    #     raise HTTPException(400, detail="Invalid document type")
    except HTTPException as e:
        e.detail
        raise


@app.post("/files/upload_department")
def upload_department_file(file: UploadFile = File(...), db=Depends(db)):
    try:
        contents = file.file.read()
        buffer = BytesIO(contents)
        df = pd.read_csv(buffer, header=None)
        df = df.rename(columns={0: "id", 1: 'department'})
        buffer.close()
        file.file.close()
        print(df.to_dict(orient='records'))
        department = DepartmentFacade(db, 'department')
        department.insert_department(df.to_dict(orient='records'))
        return {"Response": 200, "department": df.to_dict(orient='records')}
    except HTTPException as e:
        e.status_code(400)
        raise


@app.post("/files/upload_jobs")
def upload_jobs_file(file: UploadFile = File(...), db=Depends(db)):
    try:
        contents = file.file.read()
        buffer = BytesIO(contents)
        df = pd.read_csv(buffer, header=None)
        df = df.rename(columns={0: "id", 1: 'job'})
        buffer.close()
        file.file.close()
        print(df.to_dict(orient='records'))
        job = JobFacade(db, 'job')
        job.insert_job(df.to_dict(orient='records'))

        return {"Response": 200, "job": df.to_dict(orient='records')}
    except HTTPException as e:
        e.status_code(400)


@app.get("/reprt/group_q_numbers_employess/{year}")
def group_q_numbers_employess(year: int, db=Depends(db)):
    try:
        group = EmployedFacade(db)
        df = group.search_group(year)
        return {"Response": 200, 'group_q_numbers_employess': df}
    except HTTPException as e:
        e.status_code(400)


@app.get("/reprt/total_hired_employess/{year}")
def group_q_numbers_employess(year: int, db=Depends(db)):
    try:
        group = EmployedFacade(db)
        df = group.search_total(year)
        return {"Response": 200, 'group_q_numbers_employess': df}
    except HTTPException as e:
        e.status_code(400)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
