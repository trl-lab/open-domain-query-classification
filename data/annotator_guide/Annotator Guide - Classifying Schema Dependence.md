Your task is to determine if a user's query is **schema-dependent**. A query is dependent if its phrasing suggests the user has seen the underlying database structure, its specific values, or the file itself. Please evaluate each query along the following three dimensions.

### **1. Structural Reference**

**Core Question:** Does the query use terms that sound more like a database column name than a natural, conceptual question?

- **Structural Reference: `True`**
    
    - The query uses **code-like syntax** (`snake_case`, `camelCase`).
        
        - _Example: "What is the average `SalePrice`?"_
            
    - It contains **database-specific concepts** not used in everyday speech.
        
        - _Example: "List the `id` for each record."_
            
    - The phrasing is **unnatural or overly technical** for a normal question.
        
        - _Example: "Find the `satisfaction score composite`." (Instead of "How satisfied were they?")_
            
    - **Important:** Do **not** flag specialized domain jargon that an expert would naturally use (e.g., "earnings per share" in a finance context).
        
- **Structural Reference: `False`**
    
    - The query uses natural, conversational language.
        

---

### **2. Value Reference**

**Core Question:** Does the query use a specific value in a way that implies the user has already looked at the data?

- **Value Reference:`"True"`** (Clear dependence)
    
    - The query uses **internal or non-public identifiers**.
        
        - _Example: "What is the status of `order #A98Z-W`?"_
            
    - It uses **unnatural formatting** like quotes around a common word, suggesting a programmatic lookup.
        
        - _Example: "Count visitors that are `'Adult'`."_
            
    - It **describes the properties of a value** instead of just using the value.
        
        - _Example: "Find codes that start with `'SKU-'`."_
            
- **Value Reference: `"Obscure"`** (Likely dependence)
    
    - The query uses a highly specific value that is not an internal ID but is **extremely unlikely to be known without seeing the dataset first**. This is a rare category.
        
        - _Example: "Who finished the 100m sprint in `9.91s` at the 2009 world championship?" (The exact time is very "dataset-y" but someone could know this exact value from another source (e.g., Wikipedia article))._
            
- **Value Reference: `"False"`** (No dependence)
    
    - The query uses only **publicly knowable facts**, even if they are very specific. This includes:
        
        - Names of people, places, or things (e.g., "Haruki Murakami," "France").
	        
        - Specific dates or years (e.g., "September 24, 2025").


---

### **3. Container Reference**

**Core Question:** Does the query explicitly mention the data file, table, or spreadsheet it's asking about?

- **Container Reference: `True`**
    
    - The query uses words that refer to the data artifact itself. Look for terms like: **"dataset," "table," "file," "spreadsheet," "survey," "list,"** or **"records."**
        
        - _Example: "In this `file`, what is the most common entry?"_
            
        - _Example: "Based on `the survey`, what was the main opinion?"_
            
    - **Important:** A reference to a **"column"** or **"field"** is a **Structural Reference**, not a Container Reference.
        
- **Container Reference: `False`**
    
    - The query asks a direct question about the world without mentioning the data source.
        
        - _Example: "What was the main opinion in that election?"