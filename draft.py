import os

from PIL import Image
import io


def optimize_image_for_web(input_path, output_path, max_width, max_height, max_filesize_in_kb=1000):
  # Open an image file
  with Image.open(input_path) as img:
    # Resize the image
    img.thumbnail((max_width, max_height), Image.ANTIALIAS)

    # Save the image with reduced quality but keep the quality high enough
    # Start with high quality
    quality = 95
    while quality > 10:
      # Use BytesIO to temporarily save the image to memory
      with io.BytesIO() as temp_output:
        img.save(temp_output, format='JPEG', quality=quality, optimize=True)
        size_kb = temp_output.tell() / 1024  # Size in KB
        # If file is small enough, break out of the loop
        if size_kb <= max_filesize_in_kb:
          break
        # Else, reduce quality and try again
        quality -= 5

    # If the quality is 10 or below and the image is still too large,
    # it may not be possible to get it under the desired file size
    # without changing the dimensions further.
    if quality <= 10 and size_kb > max_filesize_in_kb:
      print(f"Cannot reduce file size to below {max_filesize_in_kb} KB without further reducing dimensions.")
      return False

    # Save the image with the determined quality
    img.save(output_path, format='JPEG', quality=quality)

  print(f"Image saved with quality {quality} at {output_path}, size: {size_kb:.2f} KB")
  return True

"""
for file in os.listdir(f"/Users/curryyao/Library/Mobile Documents/com~apple~CloudDocs/Git/official-website/20231031-halloween/"):
  if "jpeg" in file:

    # Example usage
    input_image_path = f'/Users/curryyao/Library/Mobile Documents/com~apple~CloudDocs/Git/official-website/20231031-halloween/{file}'
    output_image_path = f'/Users/curryyao/Library/Mobile Documents/com~apple~CloudDocs/Git/official-website/20231031-halloween/{file.replace("jpeg","jpg")}'
    max_image_width = 800  # example width
    max_image_height = 600  # example height

    # Optimize the image
    optimize_image_for_web(input_image_path, output_image_path, max_image_width, max_image_height)
"""


googlelinks = '''https://drive.google.com/open?id=1tbUcfQlpWy-DJA9qzckv61foZK7OWdsC&usp=drive_copy
https://drive.google.com/open?id=1UWKUfXcJZwu8ksDBEvklCjWz2wvjM4o_&usp=drive_copy
https://drive.google.com/open?id=1uR244_qOMqebaEeAcC_cDGITlYttHJbc&usp=drive_copy
https://drive.google.com/open?id=1TMBUWhnkUB91lUfrQ52LXm7ARQcP8LlJ&usp=drive_copy
https://drive.google.com/open?id=1ngmV79hpH69-4LeJxNhil1ZP9sXirY98&usp=drive_copy
https://drive.google.com/open?id=1E_rU3xdFXo8IFJEuYwFnwM4OurRK1JTH&usp=drive_copy
https://drive.google.com/open?id=1X_kKx2NzsUzzfgjzCzJpHmSz8_UCBa8I&usp=drive_copy
https://drive.google.com/open?id=1LdV5fuvVqBN1RHPEoAf4WrmzvyVaRel6&usp=drive_copy
https://drive.google.com/open?id=1uL4WmcCWaVZpykSipdsiMhIDgBG-38Mm&usp=drive_copy
https://drive.google.com/open?id=1eWq8D-IHDQqU0CRI5hJG2F3VojRTfxdj&usp=drive_copy
https://drive.google.com/open?id=1AeDp64mL00eS-4DYBxl14Re3o1F1s1SC&usp=drive_copy
https://drive.google.com/open?id=1NXrpnfoe9mr2CecvUejQcfui4PzMsB4o&usp=drive_copy
https://drive.google.com/open?id=1IZvE1D-2qOhFQuZk9v_fdNe0gRR9GuDw&usp=drive_copy
https://drive.google.com/open?id=1AzRLjiCPMWeaNVGP2-zHOOnQ3UlaKb2d&usp=drive_copy
https://drive.google.com/open?id=10kuWoTbIPlE8UsTqcj24LTXKV7AVOEjh&usp=drive_copy
https://drive.google.com/open?id=1a_mlxRkhZAZvi8n6kA6IyyLa7pvJAHhp&usp=drive_copy
https://drive.google.com/open?id=1wb2jFNP_prYgnSbNn9KH3xgOuRpnN9Ef&usp=drive_copy
https://drive.google.com/open?id=1gL2HVbXzWv0rOLVKFLLm2h_RRcWaTRai&usp=drive_copy
https://drive.google.com/open?id=1fbADXKBvDvOGHE78oLHezJQvyZQDXFMR&usp=drive_copy
https://drive.google.com/open?id=1s8J008QugO2M44ry8rm9Gdw6zehySswD&usp=drive_copy
https://drive.google.com/open?id=1JGgy3LgUlxOCWNWIc9DJFjUUtC69y6wE&usp=drive_copy
https://drive.google.com/open?id=1x0D9jIfnDCRsjPuLKzRTcHYF3o-6diJg&usp=drive_copy
https://drive.google.com/open?id=1hGhfyv9G1AL1HWrSRaz1Om2CsUR5_YXy&usp=drive_copy
https://drive.google.com/open?id=19rGkhqg_y7A8Cy83oKenhtT_AJ5oYvbv&usp=drive_copy
https://drive.google.com/open?id=1TQOowF0WSPvV05uo4XveeHZRZ5w7FHYW&usp=drive_copy
https://drive.google.com/open?id=1L71Uve7hOtH-QzxdmSHy3SPSQ0RTuZm6&usp=drive_copy
https://drive.google.com/open?id=1A5uc0UISNbJwS4fXimc2v5L4nGPQjqye&usp=drive_copy
https://drive.google.com/open?id=1Z9j8U2PngBMfn-EnU21wyHMVtZyeskLj&usp=drive_copy
https://drive.google.com/open?id=1RXP5Ebx6p7iCayHDANJYZM6LB-DtcP72&usp=drive_copy
https://drive.google.com/open?id=1dtH0xQ15v_nobMgwwxDvkg0jrPvgBDTW&usp=drive_copy
https://drive.google.com/open?id=1HPyJy4b9j8tXWSKQ4O9PNM1C5F_G_G3D&usp=drive_copy
https://drive.google.com/open?id=1bq5PZZfEEdLYBNWJxzGHIAOrVRyuXlqT&usp=drive_copy
https://drive.google.com/open?id=1jj__1WhojyktRWU2_CxPaai_eu53gWTf&usp=drive_copy
https://drive.google.com/open?id=1zpg6NCV1iDqbqsXsllBJObzSfZh1koZ_&usp=drive_copy
https://drive.google.com/open?id=1tkrPJsIEpm_OCVzd0-B5MBcMPgRtS4Zr&usp=drive_copy
https://drive.google.com/open?id=15xlPs5ExZCmIx69HGYYhqRVyMU_LjYKa&usp=drive_copy
https://drive.google.com/open?id=15kvnwYkE1a1xrAyUvIF_O0aMlrVEl-0g&usp=drive_copy
https://drive.google.com/open?id=107Wq6faPs-qUwDNgkE7i4A0WfHElee4m&usp=drive_copy
https://drive.google.com/open?id=13hccJL_nGyf15Wsm_zrHGRPJX1ajlo2I&usp=drive_copy
https://drive.google.com/open?id=1hnvR2nd4ga8pLAaAKMqwjKG4iMPldRtY&usp=drive_copy
https://drive.google.com/open?id=1INf8VqAvK1NCUot4DZw8jL4Xc6wtvvoO&usp=drive_copy
https://drive.google.com/open?id=1fPn4M8SUOlEzGWKulGvByyVnWaHBP6lF&usp=drive_copy
https://drive.google.com/open?id=10-1QYCM1BbKkZjF813VmDrocdaJvMWhf&usp=drive_copy
https://drive.google.com/open?id=1qCzu2ONZX_7bu_PIHtLZqPIVarOEcl_z&usp=drive_copy
https://drive.google.com/open?id=1Oy0R_Aby_28gMMGZzjFjEJzzNgm4xeT3&usp=drive_copy
https://drive.google.com/open?id=1GpMtR5S-SRM9Ly9jOkGZWU-7-IZDFWVE&usp=drive_copy
https://drive.google.com/open?id=1SMUeiGbZbzQCoPev7-7BBxLsJ-Sm2vG-&usp=drive_copy
https://drive.google.com/open?id=1xCcnVmaUQKz2gsSfsp0biPVwgCyAH1OW&usp=drive_copy
https://drive.google.com/open?id=1ZgW6mLaq3a5Rdf6K_tGoDf2U5ayc19pr&usp=drive_copy
https://drive.google.com/open?id=16QoH9YCs7VurKgL11O8_3gPRBWn4i7Nv&usp=drive_copy
https://drive.google.com/open?id=1C3-1-_CMpIudx_nugzubFspXdiTuf8cO&usp=drive_copy
https://drive.google.com/open?id=1S3tvJpw3yZoZZp_v3jWmLgH7fiR_NJlX&usp=drive_copy
https://drive.google.com/open?id=1njBJrfbdj81K6-Ojx9nDrJNdVQrL8xv_&usp=drive_copy
https://drive.google.com/open?id=1MyIneNlc96MPVr98StOuKd4a801bzL4U&usp=drive_copy
https://drive.google.com/open?id=1FuzYboezpV5QDp3K6JGAuMojW4b1I2Jq&usp=drive_copy
https://drive.google.com/open?id=1U__9JAiWxTsC0olJ01CzzRt58MQr8voz&usp=drive_copy
https://drive.google.com/open?id=1Y3VG3_RmV96uAugh5By10k2EnWHAax2s&usp=drive_copy
https://drive.google.com/open?id=1xN7PRzDCkiSYHLagMdhhDYQDSEPtI-TC&usp=drive_copy
https://drive.google.com/open?id=1R4vTnKONtGoCCEFGp2HsG6XCJcR2weGb&usp=drive_copy
https://drive.google.com/open?id=10KbGIOihbtH6jK11NziBgkGwSgO6DnLo&usp=drive_copy
https://drive.google.com/open?id=1prMmfhor9TPpimxOs4V-2PPuLp3mF4mS&usp=drive_copy
https://drive.google.com/open?id=17GoUqc7ruXKFFwM_pyi5E3-pdkRoj_GS&usp=drive_copy
https://drive.google.com/open?id=1lHt3nXaZ2xZRviSlh7YxmZrcqm2fAFsx&usp=drive_copy
https://drive.google.com/open?id=12kpOHeCLaeWBZtdQ9oNzdCpte8KAZ5VG&usp=drive_copy
https://drive.google.com/open?id=1pu9oPc-qbvdPEaySQBLgRbFizmqICiRY&usp=drive_copy
https://drive.google.com/open?id=1Mf5zRjxxsPa8k2PoKiKZgLZ82MKsYaYb&usp=drive_copy
https://drive.google.com/open?id=1YGY-hfMX1Q8XBPtKG1DuDgPvBz2DhmPT&usp=drive_copy
https://drive.google.com/open?id=15AY6swhlspuVx2NiMNHqy_lXjZsOcKTI&usp=drive_copy
https://drive.google.com/open?id=1VfMR3cWwVnPvcG0lTRTDhttpJ79-7bWd&usp=drive_copy
https://drive.google.com/open?id=1juynDPV0JQc0c9ByY7-YmEJLFEKqrdbF&usp=drive_copy
https://drive.google.com/open?id=1NRnurs2pl8x2ykdvPPsucfp-GpBshRRh&usp=drive_copy
https://drive.google.com/open?id=1bmCtdnJxWCGIT58xRPoYijoPFD_etKy1&usp=drive_copy
https://drive.google.com/open?id=1RW3jrCgczWZE6FmgcBlYAUfuUr0JBDnb&usp=drive_copy
https://drive.google.com/open?id=18wILhJIIwlRh0RwDCK1indZlawGWVJAE&usp=drive_copy
https://drive.google.com/open?id=1N5LyhFJIyNJ7gzEgEUsoAS-r_tffsotr&usp=drive_copy
https://drive.google.com/open?id=1FO4sqy7-Eb-S6yeBQBDsNUuhYPRey2Ul&usp=drive_copy
https://drive.google.com/open?id=17T55PEOkIor7lBp_8HUnqNZ8pGxh6frU&usp=drive_copy
https://drive.google.com/open?id=1dErqkAmFRF0V2siQWbIG3HVWIqV_odPc&usp=drive_copy
https://drive.google.com/open?id=1VbXCEYZAm22H7WpvnyHa8ovIZq6N_ZGw&usp=drive_copy
https://drive.google.com/open?id=1Jyo9QzHjY3t9Xh-oaqcjvGjsxHEp7ebU&usp=drive_copy
https://drive.google.com/open?id=1Fq5E_j9xZvsDxcUd9X1AxglBbYnsd8As&usp=drive_copy
https://drive.google.com/open?id=19lT8_MWtGMjMvfvKX9Ja4Q9y5X9MG8lJ&usp=drive_copy
https://drive.google.com/open?id=1xX2R2QmTyApEYkPrwMgCZsKjvlYlVj1h&usp=drive_copy
https://drive.google.com/open?id=1ttGDHRWM9C-FkOEM7k94Cyx1EVhAi55t&usp=drive_copy
https://drive.google.com/open?id=1hoCiEvVVxdjIfbmh7BoHaHdKvroqjun6&usp=drive_copy
https://drive.google.com/open?id=1GBkVSVW1YlFJ2MgidMlKTWi4SX_RLg81&usp=drive_copy
https://drive.google.com/open?id=16zSoffTW1qp4unoDdK06CjOWiLBfYZJm&usp=drive_copy
https://drive.google.com/open?id=16LD56D0QH68gpIBvyWGO9m2IgN1cEbIf&usp=drive_copy
https://drive.google.com/open?id=1kY2x07lqYoB0owSWgSWxnDZH4SO6QTfo&usp=drive_copy
https://drive.google.com/open?id=17m2_1os7z8M84g7XjA33GWTekslnUJPy&usp=drive_copy
https://drive.google.com/open?id=1Lw94oRTBoMhtiOUmx0xCWZQc4_hKLhB7&usp=drive_copy
https://drive.google.com/open?id=11YdQn3js6x-3_6Z_6tLGnR850E8E0nez&usp=drive_copy
https://drive.google.com/open?id=109WSuUoHkibXVpEwHUYLumCNq8CrWOVN&usp=drive_copy
https://drive.google.com/open?id=1v0voYJFp9rwj7Il2K0y0PcuAWU3HHRfM&usp=drive_copy
https://drive.google.com/open?id=1kfuPcGV84UsP3XHwnXe1SQwMoNmZbCJ8&usp=drive_copy
https://drive.google.com/open?id=1Qsvj2RLJl1Qq_sEPLiVJnIJnMAjemb8c&usp=drive_copy
https://drive.google.com/open?id=1XgA2m93PIttGqyXx8effTA0ten8RcwRz&usp=drive_copy
https://drive.google.com/open?id=1DiMYyWSKt4DxOkCd8MJ9i5YYRMgNnwGe&usp=drive_copy
https://drive.google.com/open?id=1_4nSq5zKFXYv1GwTfPIuDMYmvmOXTric&usp=drive_copy
https://drive.google.com/open?id=1p2L-xUylYG-waCy28vBhRGH68-0Zo7VN&usp=drive_copy
https://drive.google.com/open?id=1_ikQE9WTBbPsfamxL_NE5qyQbVLJfTrP&usp=drive_copy
https://drive.google.com/open?id=1QOnJHoWKcHMJTdhcH0DtA67jVsbLoTGP&usp=drive_copy
https://drive.google.com/open?id=1Wg9HIZrM4CwQwPQnjBgGyKOit2C2kpaY&usp=drive_copy
https://drive.google.com/open?id=13m1ff1O6x6Z8SSw0HIJFRhSk0HNbxSc9&usp=drive_copy
https://drive.google.com/open?id=18Qb0bSEGZ6LcEP6RTJVTuePz8uu8MRPQ&usp=drive_copy
https://drive.google.com/open?id=1OkL6exgdIVE0jqPhCN8Tj3jQcD_v52F6&usp=drive_copy
https://drive.google.com/open?id=1Ql8yVjRc7TT1jEX2CkoTmcWJVhkUvUfO&usp=drive_copy
https://drive.google.com/open?id=16KSreSIoTq-_V0gJlENUygjvSFKVC8tN&usp=drive_copy
https://drive.google.com/open?id=167SzjpDRQQ5lBFKFbE5IjvjB9re4O8xc&usp=drive_copy
https://drive.google.com/open?id=1a2xYR7X7XF7BT9LO7oB8UAHec2eFx44W&usp=drive_copy
https://drive.google.com/open?id=1NOZSucKo3LABT3J9FBlt6ZobsjFi9TpG&usp=drive_copy
https://drive.google.com/open?id=1WBHynQAUajvR7NIVjyXhBFKZmlsIO__P&usp=drive_copy
https://drive.google.com/open?id=1MvZFOMCgRzzSMqK4yaaPiz8pPmO1K4H8&usp=drive_copy
https://drive.google.com/open?id=1ZUD8fkavbvzPW0PQu-woAVohq9RpvXcO&usp=drive_copy
https://drive.google.com/open?id=1ANG-QptzyXAEEBKdMGPrlKiP34DlwKJE&usp=drive_copy
https://drive.google.com/open?id=1EF-Z_z0jhSNDEOoGYJ8w35MRUfhrxNfh&usp=drive_copy
https://drive.google.com/open?id=1gDXaDfJ7vFINhT4WY1DBIx6AQBuUjPnX&usp=drive_copy
https://drive.google.com/open?id=1qmVdiSUI9VfM80TWrX5LgZgsD3_-yAO2&usp=drive_copy
https://drive.google.com/open?id=1svVgY_UKZS9wnH3mbS86BS7wbc8_CVhe&usp=drive_copy
https://drive.google.com/open?id=1IQztGLslXz2Qiy41qb5IUGa_xY6PXUeO&usp=drive_copy
https://drive.google.com/open?id=1oQjohZWi3_ow6qbOFu38SYGuD3A3p8Jp&usp=drive_copy
https://drive.google.com/open?id=1CGopr-exnI96tXpoSTm-HHc5WR_cTCVm&usp=drive_copy
https://drive.google.com/open?id=1imUBhqJg9dZ0AOuSbEIcwMALlZ9t6tgQ&usp=drive_copy
https://drive.google.com/open?id=18QRo-44V_NHsgYPBJK89REENcq1ApMvO&usp=drive_copy
https://drive.google.com/open?id=1h1miOYmFuLqFNduBCr2_Ahoet1X_-T1a&usp=drive_copy
https://drive.google.com/open?id=1TflyPARasOfvST00GugLhPtFO-FVmtd-&usp=drive_copy
https://drive.google.com/open?id=11EUkoTiHpgLo8SObWmr20l0QB0lnJxJt&usp=drive_copy
https://drive.google.com/open?id=1EpTrwACjPrGbxt3cQTF2fQtQx1zszv8U&usp=drive_copy
https://drive.google.com/open?id=1tb65--i7VSQF9nzRc43rI3Gfux-0iXt9&usp=drive_copy
https://drive.google.com/open?id=1Untsra2zqGSVnF_gJiBYw5XkYakRlRKE&usp=drive_copy
https://drive.google.com/open?id=1jY3wdHMcQD5QKqhoVtPllL1EStTm4SmR&usp=drive_copy
https://drive.google.com/open?id=1e72ME6QywQSFMaJkhpzXPGnPbc4tXb5q&usp=drive_copy
https://drive.google.com/open?id=1-wg_MKNpWqgd78xTy2HRbOvQsMKfJsPG&usp=drive_copy
https://drive.google.com/open?id=1GycdJ3i6S67EYUfu-WZ2DMmu6sc5Y2qb&usp=drive_copy
https://drive.google.com/open?id=1sIh8tepIrof-8m2vDul6gZYadpemfL4W&usp=drive_copy
https://drive.google.com/open?id=1i6JiPTAIsb1-OOchYEIaOe5J_dzTVE6O&usp=drive_copy
https://drive.google.com/open?id=1rvmiFx9aTt0IWzt_zWus9WbSn8QSdlQG&usp=drive_copy
https://drive.google.com/open?id=1iXxwz3lOBOAhbuvNH14w9aLE8Ztrb5I3&usp=drive_copy
https://drive.google.com/open?id=1b_t54n7ZnzVOnsJfEqV8d_QAtz4GqtsT&usp=drive_copy
https://drive.google.com/open?id=1eFWxyjfviStTIHfj5GFHBu11i6t8clYi&usp=drive_copy
https://drive.google.com/open?id=1uJAOtWzRb4xF6T4Zpvif-OiNNfbSZhlO&usp=drive_copy
https://drive.google.com/open?id=1QaJHm6jkYufxaATBKfJ0G9nIHAhXYYTF&usp=drive_copy
https://drive.google.com/open?id=1P958F1IQkzut_v5CU2y-tRRVJXJjZ_md&usp=drive_copy
https://drive.google.com/open?id=1TAjzHlxWvaYPCRhn8QhUqM4H10704JMx&usp=drive_copy
https://drive.google.com/open?id=1he6ALzV4spmNYpPQUHPZt1YC2XRvJphQ&usp=drive_copy
https://drive.google.com/open?id=1Gt42XY5gMKroxoRT7lRMevgSh3BVALW0&usp=drive_copy
https://drive.google.com/open?id=19MRl95zWlKBiWrJEXdlunRXd0qRZs1Id&usp=drive_copy
https://drive.google.com/open?id=1r4frNTjvSJbLmS3bC-9N8BzsmiT1Jnot&usp=drive_copy
https://drive.google.com/open?id=1p0esjeoVomwiuU8iUBw7TIOh3GlrJ81p&usp=drive_copy
https://drive.google.com/open?id=1Ugaa5ZDlHXwqIjAs4IP3f1dXFpvZwDdw&usp=drive_copy
https://drive.google.com/open?id=1JvzIBANFTKjC8RXbJCLId2JLPY4bQ2ur&usp=drive_copy
https://drive.google.com/open?id=1r7jByqUr35IsGYZxP_YcylvSfRmqIsHt&usp=drive_copy
https://drive.google.com/open?id=1E-DeMEOjzmBu6Zo_4CwdisQBwMimvu3j&usp=drive_copy
https://drive.google.com/open?id=1GQvdZbMbzsM6HDem3F5f-a6jDHSr0X_T&usp=drive_copy
https://drive.google.com/open?id=1DE2-Osy-B-kN9z09DCAfsACWTlh8jgPN&usp=drive_copy
https://drive.google.com/open?id=1k8EbrU3nV5jGOUAUdaluYPsjEKGNj7QS&usp=drive_copy
https://drive.google.com/open?id=1lHd1whis3bwUGMnZXCo31TXnd9BAZ-02&usp=drive_copy
https://drive.google.com/open?id=1hgX8J1zah0H5DpIY191DDXhANGJwzb9k&usp=drive_copy
https://drive.google.com/open?id=1wdZo8aQ_DxYiYSZwnwmVfxgUORRKwcHS&usp=drive_copy
https://drive.google.com/open?id=1vyjykNjr61HidG1hc_UNxXv9_mPQ88R9&usp=drive_copy
https://drive.google.com/open?id=1fS_HuP2JEhPgoYbCAzBvAiqkdS1jXyij&usp=drive_copy
https://drive.google.com/open?id=1Gh8ZjBUJfTOzOZVNbdfYnsXyLuz1VBnC&usp=drive_copy
https://drive.google.com/open?id=100YQidnvMOqbWfaApNVwQ7a3Sn1yGbFQ&usp=drive_copy
https://drive.google.com/open?id=1YVTbxvI3O9bNIvH3Q8ygMWKeL3iglzk1&usp=drive_copy
https://drive.google.com/open?id=1HV4dCr9PiKQnH2Kv4M52UvEUfi2JfKrA&usp=drive_copy
https://drive.google.com/open?id=1fABw5ZzDQOMmVPlTP0S8In3NuEerGAQx&usp=drive_copy
https://drive.google.com/open?id=1GjRWrR-kxu9QFeJSWwvzO-FcXpOg_tVp&usp=drive_copy
https://drive.google.com/open?id=1vXTMACa4asO0XGdg7BUvsgqm3uTyMyx-&usp=drive_copy
https://drive.google.com/open?id=1KHe4ZpYv-oRTMHuIoHcXPgXz3SvbBC6o&usp=drive_copy
https://drive.google.com/open?id=10LzMqHB0blDp6zg7yLe9M9Ex6dcjwqx-&usp=drive_copy
https://drive.google.com/open?id=19REClj7ee-qE8PwRO2portoNKT6NuyiD&usp=drive_copy
https://drive.google.com/open?id=1NJsMk0EikaRMdLb5ZTJor_-2fV4ADmHa&usp=drive_copy
https://drive.google.com/open?id=1h1Z16BrfeJVylq6E4O34U79dz8PseKFb&usp=drive_copy
https://drive.google.com/open?id=1SCwf0kq_mWPl14B7QPFeY768M0T8nNab&usp=drive_copy
https://drive.google.com/open?id=1nTeMtws32vKIxFwXkkh02g3hUwYzvAuL&usp=drive_copy
https://drive.google.com/open?id=1XK3dOHtevp-NmdvfOryUHBlo3iXoSbQe&usp=drive_copy
https://drive.google.com/open?id=1RS2Xj5hTWu3mCpgPw1wABqCpquriFzrW&usp=drive_copy
https://drive.google.com/open?id=1bbWt0wG26hBWYbYiZdtoT5V_k2CVHY9M&usp=drive_copy
https://drive.google.com/open?id=1nfqmJ7bCCSrUTL4Gg3HcYheR2ge-mjYB&usp=drive_copy
https://drive.google.com/open?id=10oZPJp8ECBuSn45A2Oe-HRge-YVm6lvO&usp=drive_copy
https://drive.google.com/open?id=1xiWlFBv5ijJ6InFNtaxwv1SA5TQFZ9lO&usp=drive_copy
https://drive.google.com/open?id=17UPUYYKGYYZC9kqLcQra1OzuT4T1F4ZF&usp=drive_copy
https://drive.google.com/open?id=1JY3F7XaBSTrNKRuR0KvtYf1AKOXc8269&usp=drive_copy
https://drive.google.com/open?id=1mQQlo3X64yXjHSr9yw4JQ1TafldXzSTm&usp=drive_copy
https://drive.google.com/open?id=1prkFvnvNnZLwJWiyM0wRMYv2McHgxJ_E&usp=drive_copy
https://drive.google.com/open?id=1nj1MkWQ3fXA3Hu37zJhJV8eqGWlVFNLv&usp=drive_copy
https://drive.google.com/open?id=1DGu0kQ7QC5IENY0EPE7mwIOZ61sQ13Yf&usp=drive_copy
https://drive.google.com/open?id=1MaIhf_tbZDa7yhIT-jKaKo1gnM3vUgZo&usp=drive_copy
https://drive.google.com/open?id=1lfl7ry124skJKgpu113eJx0OnzehSQcB&usp=drive_copy
https://drive.google.com/open?id=1dOW82yjjlerLvWa6X-kkkMyK4Bkoc3Ms&usp=drive_copy
https://drive.google.com/open?id=1FDmhn9ajMZd59Noxhw0kuaHgydnpwqC5&usp=drive_copy
https://drive.google.com/open?id=1OMdS-R2ecLzpuN5h4FhG53tN1-IjU1pE&usp=drive_copy
https://drive.google.com/open?id=17OjSuNPQz1NEoxdWq9wcKqRapLkVcK10&usp=drive_copy
https://drive.google.com/open?id=10Fbety8cAVRxx0jGYhoox_Hx2IvgkEwT&usp=drive_copy
https://drive.google.com/open?id=1uRnklCj2SKn9orVbY1Lc4nsJTYsKfq_R&usp=drive_copy
https://drive.google.com/open?id=1pftGeWIhSV_IoscJsv4bbCZrXzjL3RfB&usp=drive_copy
https://drive.google.com/open?id=1ynPhnEJKEe_7uenYyPVpinkXkPhReZo7&usp=drive_copy
https://drive.google.com/open?id=194GbbxZDgPG_Pcc7B3cZ3TowS2c2OnmK&usp=drive_copy
https://drive.google.com/open?id=1qFkij3PEebexinKmmM-z6kfimls8r1n8&usp=drive_copy
https://drive.google.com/open?id=1b0fJ6Uf_6r4kU8TdMOEiM4bhPYoGZbNV&usp=drive_copy
https://drive.google.com/open?id=1gjfWwnxbb5LIF1_wqt37zAf3r1Xi1m2N&usp=drive_copy
https://drive.google.com/open?id=1uJWOtuLrlDxUnl4gxaNjyV7mKlvC8eDi&usp=drive_copy
https://drive.google.com/open?id=16q7qGQ9EICMs6Sb2Cc9mY-EFyKttlapE&usp=drive_copy
https://drive.google.com/open?id=1cP0a8gjLgkhwsfoQ7dEJEmHJpHYHFwCg&usp=drive_copy
https://drive.google.com/open?id=1oAzIU_kabzEAEiGoTjYq6SC3Xi_KK4qr&usp=drive_copy
https://drive.google.com/open?id=1eYcgWcrKsGc0jVNcUmDCastIm1krXDtg&usp=drive_copy
https://drive.google.com/open?id=1Y2GgI1UDkOdhRwQ_iq4g7WyY9IMb4Ik3&usp=drive_copy
https://drive.google.com/open?id=1-_DgCm-Pd_rby-KNcWyivHSYMzEUj3Ko&usp=drive_copy'''.split('\n')
googlelinks = [i.replace('open?','uc?export=download&') for i in googlelinks]

names = '''_EDS2727.JPG
_EDS2728.JPG
_EDS2729.JPG
_EDS2730.JPG
_EDS2731.JPG
_EDS2732.JPG
_EDS2733.JPG
_EDS2734.JPG
_EDS2735.JPG
_EDS2736.JPG
_EDS2737.JPG
_EDS2738.JPG
_EDS2739.JPG
_EDS2740.JPG
_EDS2741.JPG
_EDS2742.JPG
_EDS2743.JPG
_EDS2744.JPG
_EDS2745.JPG
_EDS2746.JPG
_EDS2747.JPG
_EDS2748.JPG
_EDS2749.JPG
_EDS2750.JPG
_EDS2751.JPG
_EDS2752.JPG
_EDS2753.JPG
_EDS2754.JPG
_EDS2755.JPG
_EDS2756.JPG
_EDS2757.JPG
_EDS2758.JPG
_EDS2759.JPG
_EDS2760.JPG
_EDS2761.JPG
_EDS2762.JPG
_EDS2763.JPG
_EDS2764.JPG
_EDS2765.JPG
_EDS2766.JPG
_EDS2767.JPG
_EDS2768.JPG
_EDS2769.JPG
_EDS2770.JPG
_EDS2771.JPG
_EDS2772.JPG
_EDS2773.JPG
_EDS2774.JPG
_EDS2775.JPG
_EDS2776.JPG
_EDS2777.JPG
_EDS2778.JPG
_EDS2779.JPG
_EDS2780.JPG
_EDS2781.JPG
_EDS2782.JPG
_EDS2783.JPG
_EDS2784.JPG
_EDS2785.JPG
_EDS2786.JPG
_EDS2787.JPG
_EDS2788.JPG
_EDS2789.JPG
_EDS2790.JPG
_EDS2791.JPG
_EDS2792.JPG
_EDS2793.JPG
_EDS2794.JPG
_EDS2795.JPG
_EDS2796.JPG
_EDS2797.JPG
_EDS2798.JPG
_EDS2799.JPG
_EDS2800.JPG
_EDS2801.JPG
_EDS2802.JPG
_EDS2803.JPG
_EDS2804.JPG
_EDS2805.JPG
_EDS2806.JPG
_EDS2807.JPG
_EDS2808.JPG
_EDS2809.JPG
_EDS2810.JPG
_EDS2811.JPG
_EDS2812.JPG
_EDS2813.JPG
_EDS2814.JPG
_EDS2815.JPG
_EDS2816.JPG
_EDS2817.JPG
_EDS2818.JPG
_EDS2819.JPG
_EDS2820.JPG
_EDS2821.JPG
_EDS2822.JPG
_EDS2824.JPG
_EDS2825.JPG
_EDS2826.JPG
_EDS2827.JPG
_EDS2828.JPG
_EDS2829.JPG
_EDS2830.JPG
_EDS2831.JPG
_EDS2832.JPG
_EDS2833.JPG
_EDS2834.JPG
_EDS2835.JPG
_EDS2836.JPG
_EDS2837.JPG
_EDS2838.JPG
_EDS2839.JPG
_EDS2840.JPG
_EDS2841.JPG
_EDS2842.JPG
_EDS2843.JPG
_EDS2844.JPG
_EDS2845.JPG
_EDS2846.JPG
_EDS2847.JPG
_EDS2848.JPG
_EDS2849.JPG
_EDS2850.JPG
_EDS2851.JPG
_EDS2852.JPG
_EDS2853.JPG
_EDS2854.JPG
_EDS2855.JPG
_EDS2856.JPG
_EDS2857.JPG
_EDS2858.JPG
_EDS2859.JPG
_EDS2860.JPG
_EDS2861.JPG
_EDS2862.JPG
_EDS2863.JPG
_EDS2864.JPG
_EDS2865.JPG
_EDS2866.JPG
_EDS2867.JPG
_EDS2868.JPG
_EDS2869.JPG
_EDS2870.JPG
_EDS2871.JPG
_EDS2872.JPG
_EDS2873.JPG
_EDS2874.JPG
_EDS2875.JPG
_EDS2876.JPG
_EDS2877.JPG
_EDS2878.JPG
_EDS2879.JPG
_EDS2880.JPG
_EDS2881.JPG
_EDS2882.JPG
_EDS2883.JPG
_EDS2885.JPG
_EDS2886.JPG
_EDS2887.JPG
_EDS2888.JPG
_EDS2891.JPG
_EDS2892.JPG
_EDS2893.JPG
_EDS2894.JPG
_EDS2895.JPG
_EDS2896.JPG
_EDS2897.JPG
_EDS2898.JPG
_EDS2899.JPG
_EDS2900.JPG
_EDS2901.JPG
_EDS2902.JPG
_EDS2903.JPG
_EDS2904.JPG
_EDS2905.JPG
_EDS2906.JPG
_EDS2907.JPG
_EDS2908.JPG
_EDS2909.JPG
_EDS2910.JPG
_EDS2911.JPG
_EDS2913.JPG
_EDS2914.JPG
_EDS2915.JPG
_EDS2916.JPG
_EDS2917.JPG
_EDS2918.JPG
_EDS2919.JPG
_EDS2920.JPG
_EDS2921.JPG
_EDS2922.JPG
_EDS2923.JPG
_EDS2924.JPG
_EDS2925.JPG
_EDS2926.JPG
_EDS2927.JPG
_EDS2928.JPG
_EDS2929.JPG
_EDS2930.JPG
_EDS2931.JPG
_EDS2932.JPG
_EDS2933.JPG
_EDS2934.JPG
_EDS2935.JPG
_EDS2936.JPG
_EDS2937.JPG
_EDS2938.JPG
_EDS2939.JPG'''.split('\n')

for name, googlelink in zip(names, googlelinks):
  print(f"""
    <!-- Image card {name.split('EDS')[1].replace('.JPG','')} -->
  <div class="image-card">
    <img src="20231031-halloween/{name.replace('JPG','jpg')}" alt="{name.replace('JPG','jpg')}">
    <a class="download-btn" href="{googlelink}">Download</a>
  </div>
  """)
