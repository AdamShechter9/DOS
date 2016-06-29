from system.core.controller import *


class Jobs(Controller):
    def __init__(self, action):
        super(Jobs, self).__init__(action)
        self.load_model('Job')
        self.load.model('User')
        self.db = self._app.db

    def joblist(self):
        # Show wall of jobs. Render
        all_jobs = self.model['Job'].get_all_jobs()
        return self.load_view('jobs/joblist.html', all_jobs=all_jobs)

    def addnew(self):
        # Page for adding new job. Render.
        return self.load_view('jobs/addnew.html')

    def show(self, job_id):
        # Show job by job_id. Render
        job = self.model['Job'].get_job_by_id(job_id)
        return self.load_view('/jobs/show.html', job=job)

    def edit(self, job_id):
        # Edit job by job_id. Render
        job = self.model['Job'].get_job_by_id(job_id)
        return self.load_view('jobs/edit.html', job=job)

    def create(self):
        # Process create job. Redirect
        input_form = form.request
        create_status = self.model['Job'].create_job(input_form)
        if create_status['status']:
            return redirect('/jobs/show/' + create_status['job_id'])
        else:
            return redirect('jobs/addnew')

    def update(self, job_id):
        # Process update job. Redirect
        input_form = form.request
        update_status = self.model['Job'].update_job(input_form, job_id)
        if update_status['status']:
            return redirect('/jobs/show/' + update_status['job_id'])
        else:
            return redirect('/jobs/edit/' + update_status['job_id'])

    def confirm(self, job_id):
        # Process job status to 'closed'. Redirect
        self.model['Job'].job_change_status(job_id, 1)
        return redirect('/jobs/show/' + job_id)

    def destroy(self, job_id):
        # Process destroy job. Redirect
        self.model['Job'].destroy_job(job_id)
        return redirect('/jobs/joblist')