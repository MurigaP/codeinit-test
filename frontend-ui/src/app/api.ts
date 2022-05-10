import { environment } from '../environments/environment';
export let serverurl = environment.backendApiUrl;
export let DocumentUploadApiUrl = serverurl + 'iatidoc';
export let DocumentApiUrl = serverurl + 'documents';