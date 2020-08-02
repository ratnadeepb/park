from park.param import config


def generate_job(np_random):
    # pareto distribution
    # size = 500 # homogeneous tasks
    size = int((np_random.pareto(
        config.job_size_pareto_shape) + 1) *
        config.job_size_pareto_scale)

    # restrict the maximum size of the job
    if size > config.job_size_pareto_scale * 100:
        size = int(config.job_size_pareto_scale * 100)

    # size = int(np_random.uniform(500, 2500))

    t = int(np_random.exponential(config.job_interval))

    return t, size


def generate_jobs(num_stream_jobs, np_random):

    # time and job size
    all_t = []
    all_size = []

    # generate streaming sequence
    t = 0
    for _ in range(num_stream_jobs):
        dt, size = generate_job(np_random)
        t += dt
        all_t.append(t)
        all_size.append(size)

    return all_t, all_size
