import { Component, OnInit } from '@angular/core';
import { DocumentApiUrl, DocumentUploadApiUrl } from './api';
export interface Documents {
  id: string;
  original_file_name: string;
  file: string;
  created_at: string;
  created_by: {
    username: string;
    email: string;

  };
}
import { ApiService } from './services/api.service';
import { NotificationService } from './services/notification.service';
import {
  FormGroup, FormBuilder, FormControl, Validators
} from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  FileUploadForm: FormGroup;
  title = 'Document APP';
  documents: Documents[] = [];
  isUploadSectionCollapsed = true;
  fileData: File | any = null;


  constructor(public apiService: ApiService, private formBuilder: FormBuilder, public notificationService: NotificationService) {
    this.FileUploadForm = this.formBuilder.group({
      file: new FormControl('', [Validators.required]),
      fileSource: new FormControl('', [Validators.required])
    });

  }

  ngOnInit() {

    this.listDocuments();

  }
  // Fetching all uploaded documents
  listDocuments() {
    const payload = {}
    this.apiService.getRecord(DocumentApiUrl, payload).then((data: any) => {
      if (data) {
        this.documents = data.results;
        console.log("  this.documents", this.documents)
      }

    });
  }

  // Document Upload Api Call function
  uploadDocument() {
    const formData = new FormData();
    formData.append('file', this.FileUploadForm.value["fileSource"]);
    this.apiService.postRecord(DocumentUploadApiUrl, formData).then((data: any) => {
      if (data) {
        let uploadedDocumentId = data?.document_id;
        let message = "Document upload was successful. Document id :" + uploadedDocumentId
        this.notificationService.showSweetAlert("Success", message, "success")
        // on success refresh the data async
        this.listDocuments();





      }

    });
  }
  // custom event handling for file input change
  onFileChange(event: any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.FileUploadForm.patchValue({
        fileSource: file
      });
    }

  }


}
