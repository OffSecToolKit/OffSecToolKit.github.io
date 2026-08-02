---
layout: page
title: OffSecToolKit
---

<div class="hero" markdown="1">
![logo]({{ site.url }}/assets/logo.png){:.logo}

OffSecToolKit is an interactive cheat sheet, containing a curated list of offensive security tools and their respective commands.
</div>

If you hate constantly looking up the right command to use while conducting CTFs or Offensive Security enagements, this project should help ease the pain a bit. Just select what phase you are currently in or what services are open and it will display a list of tools you can try against the machine, along with a template command for easy copy/pasting. See the full list of [items](/items/) and [filters](/filters/).

This project was created by [Tony Harkness](https://www.linkedin.com/in/tonyharkness) and was inspired by [GTFOBins][GTFOBins] and [LOLBAS][LOLBAS]. I relied heavily on [GTFOBins'][GTFOBins] site template to make this one.

I'm hoping to make OffSecToolKit a [collaborative project][collaborative], so please feel free to [contribute][contribute] your commands.

[items]: {{ site.url }}/items/
[filters]: {{ site.url }}/filters/
[GTFOBins]: https://gtfobins.github.io/
[LOLBAS]: https://lolbas-project.github.io/
[collaborative]: https://github.com/OffSecToolKit/OffSecToolKit.github.io
[contribute]: {{ site.url }}/contribute/

{% include bin_table.html %}
