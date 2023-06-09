from flask import Flask, Blueprint, render_template, request, send_file

from src.insights.jobs import (
    read,
    get_unique_job_types,
    filter_by_job_type,
)
from src.insights.industries import (
    get_unique_industries,
    filter_by_industry,
)

from src.insights.salaries import (
    filter_by_salary_range,
    get_min_salary,
    get_max_salary,
)

from src.flask_app.more_insights import (
    slice_jobs,
    get_int_from_args,
    build_jobs_urls,
)

from src.flask_app.more_insights import get_job

bp = Blueprint("client", __name__, template_folder="templates")


@bp.route("/.images/job.png")
def flask_image():
    return send_file("../../.images/job.png", mimetype="image/png")


@bp.route("/")
def index():
    md = """
<p align="center">
    <img src="/.images/job.png" alt="Logo da Aplicação" width="800"/>
</p>
<h2 align="center">
    Boas-vindas ao Job Insights<br><br>
</h2>
        """
    return render_template("index.jinja2", md=md)


@bp.route("/jobs")
def list_jobs():
    first_job = get_int_from_args("first_job", 0)
    amount = get_int_from_args("amount", 20)
    salary = get_int_from_args("salary", None)
    industry = request.args.get("industry", None)
    job_type = request.args.get("job_type", None)

    jobs = read(path="data/jobs.csv")
    if industry:
        jobs = filter_by_industry(jobs, industry)
    if job_type:
        jobs = filter_by_job_type(jobs, job_type)
    if salary:
        jobs = filter_by_salary_range(jobs, salary)

    jobs = slice_jobs(jobs, first_job, amount)

    build_jobs_urls(jobs)

    ctx = {
        "jobs": jobs,
        "industries": sorted(get_unique_industries("data/jobs.csv")),
        "job_types": sorted(get_unique_job_types("data/jobs.csv")),
        "previous_job_type": job_type,
        "previous_first": first_job,
        "previous_amount": amount,
        "previous_industry": industry,
        "previous_salary": salary,
        "min_salary": get_min_salary("data/jobs.csv"),
        "max_salary": get_max_salary("data/jobs.csv"),
    }

    return render_template("list_jobs.jinja2", ctx=ctx)


def init_app(app: Flask):
    app.register_blueprint(bp)


# Requisitos Bônus
# 13 - (Bônus) Implemente a página de um job
# Implemente em: src/flask_app/routes_and_views.py

#  Para fechar com chave de ouro, que tal testar o quanto você consegue
# aprender de Flask apenas vendo como fizemos as páginas de index e de jobs,
# e tentar criar uma página que irá exibir todas as informações de um job
# em específico?

# 13.1 - Crie a rota /job recebendo o parâmetro index
# A função deve ser decorada com a rota /job/<index>.
@bp.route("/job/<index>")
# 13.2 - Crie a view job, recebendo o parâmetro index
# A função deve se chamar job. A função deve receber um parâmetro index.
def job(index):
    #  13.3 - Implemente view job para que ela retorne status code 200 para
    # jobs válidos
    # A função deve chamar a read para ter uma lista com todos os jobs.
    all_jobs = read("data/jobs.csv")
    #  A função deve chamar a get_job, declarada no arquivo
    # src/flask_app/more_insights.py, para selecionar um job específico pelo
    # index.
    job_index = get_job(all_jobs, index)
    #  13.4 - Implemente view job de forma a retornar o HTML exato de uma
    # página de job
    #  A função deve renderizar o template job.jinja2, passando um parâmetro
    # job contendo o job retornado pela get_job.
    job_page = render_template("job.jinja2", job=job_index)
    return job_page
