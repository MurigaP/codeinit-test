import { Component, OnInit } from '@angular/core';
import { DocumentApiUrl } from './api';
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
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Document APP';
  documents: Documents[] = [];
  constructor(public apiService: ApiService) { }

  ngOnInit() {
    this.listDocuments();

  }
  // Fetching all uploaded documents
  listDocuments() {
    const payload = {}
    this.apiService.getRecord(DocumentApiUrl, payload).then((data: any) => {
      if (data) {
        this.documents = data.results;
      }

    });
  }

}
