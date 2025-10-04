window.addEventListener('DOMContentLoaded', () => {
    const inputFiles = document.querySelectorAll('input[type="file"]')
    inputFiles.forEach((inputFile)=>{
        inputFile.addEventListener("change",(e)=>{
            const label = document.querySelector('input[type="file"]~label')
            if(label){
                const file = e.target.files
                if(file.length>0){
                    label.textContent =`Chosen:${file[0].name}. Click to choose another`
                }
            }
        })
    })
})


