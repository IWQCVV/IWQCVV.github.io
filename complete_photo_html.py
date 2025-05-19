# generate HTML for 36 photos and write to txt file

str_photos = ""


for i in range(1, 37):
    # Generate HTML for each photo
    str_photos += f"""
            <a href="renamed_photos/{str(i).zfill(3)}.webp" class="gallery-item">
                <div class="group relative rounded-xl overflow-hidden transform transition hover:scale-105">
                    <img src="thumbs/{str(i).zfill(3)}.webp" 
                         class="w-full h-64 object-cover"
                         alt="Workshop session"
                         loading="lazy">
                    <div class="absolute inset-0 bg-black/40 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                        <i class="fas fa-expand text-3xl text-white"></i>
                    </div>
                </div>
            </a>
            """
    
# Write the txt to a file
with open("photos.txt", "w") as f:
    f.write(str_photos)


    


