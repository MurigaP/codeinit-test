import { environment } from '../environments/environment';
export let serverurl = environment.backendApiUrl;
export let DocumentUploadApiUrl = serverurl + 'iatidoc';
export let DocumentApiUrl = serverurl + 'documents';
export let default_page = 1;
export let default_page_size = 10;