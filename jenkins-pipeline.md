graph TD
    %% Stylizacja
    classDef stage fill:#f9f,stroke:#333,stroke-width:2px;
    classDef success fill:#d4edda,stroke:#28a745,stroke-width:1px;
    classDef warning fill:#fff3cd,stroke:#ffc107,stroke-width:1px;

    Start([Start Pipeline]) --> Checkout[Checkout Kodu]:::stage
    Checkout --> Build[Budowanie Aplikacji]:::stage
    
    subgraph Testy i Jakość
        Build --> Test[Testy Jednostkowe]:::stage
        Build --> StaticAnalysis[Analiza Statyczna Kodu]:::stage
        Build --> Security[Skanowanie Bezpieczeństwa SAST/DAST]:::stage
    end

    Test --> DockerBuild[Budowanie Obrazu Docker]:::stage
    StaticAnalysis --> DockerBuild
    Security --> DockerBuild

    DockerBuild --> IntegrationTest[Testy Integracyjne]:::stage

    IntegrationTest --> Staging[Wdrożenie na Staging]:::success
    
    Staging --> Approval{Akceptacja Ręczna / Gates}:::warning
    
    Approval -->|Zatwierdzone| Production[Wdrożenie na Produkcję]:::success
    Approval -->|Odrzucone| Abort([Przerwane / Rollback])
    
    Production --> End([Koniec Pipeline])