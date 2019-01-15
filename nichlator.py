#!/usr/bin/env python3
import json
import os
import subprocess
import sys

translation_file = sys.stdin.read()

translation = json.loads(translation_file)

for page in translation['pages']:
    imagemagick_name = "convert" # name of ImageMagick in your system
    text_clouds_path=os.path.join("pages", "{}".format(page['page_number']))

    os.makedirs(text_clouds_path, exist_ok=True)
    text_cloud_num = 1
    for text_cloud in page['text_clouds']:
        output_file = "{}/{}.png".format(text_clouds_path, text_cloud_num)

        # generating ImageMagick command
        im_call = [
            "{}".format(imagemagick_name),
            "-background",
            "none",
        ]

        # if these settings exists in input JSON file,
        if "font" in text_cloud:
            im_call.append("-font")
            im_call.append("{}".format(text_cloud['font']))
        """ WIP
        if "stroke_width" in text_cloud:
            # add it to the command list
            #im_call.append("-strokewidth")
            #im_call.append("{}".format(text_cloud['stroke_width']))
            if "stroke_color" in text_cloud:
                im_call.append("-stroke")
                im_call.append("{}".format(text_cloud['stroke_color']))
                im_call.append("-fill")
                im_call.append("{}".format(text_cloud['stroke_color']))
            if "alignment" in text_cloud:
                im_call.append("-gravity")
                im_call.append(text_cloud['alignment'])
            if "size" in text_cloud:
                im_call.append("-pointsize")
                im_call.append("{}".format(text_cloud['size'] +
                                           text_cloud['stroke_width']))
            if "interline_size" in text_cloud:
                im_call.append("-interline-spacing")
                im_call.append("{}".format(text_cloud['interline_size']))
            im_call.append("label:{}".format(text_cloud['text']))
            im_call.append()"{}".format(text_cloud['text']))
            im_call.append("{}".format(text_cloud['font']))
        """
        if "size" in text_cloud:
            im_call.append("-pointsize")
            im_call.append("{}".format(text_cloud['size']))
        if "alignment" in text_cloud:
            im_call.append("-gravity")
            im_call.append(text_cloud['alignment'])
        if "interline_size" in text_cloud:
            im_call.append("-interline-spacing")
            im_call.append("{}".format(text_cloud['interline_size']))

        # adding required arguments
        im_call.append("-fill")
        im_call.append("{}".format(text_cloud['color']))
        im_call.append("label:{}".format(text_cloud['text']))
        im_call.append(output_file)

        subprocess.call(im_call)

        print("converted {} text label of page {}".format(text_cloud_num,
                                                          page['page_number']))
        text_cloud_num += 1

