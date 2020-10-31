import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H5("References", className="text-left")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='In order for our research to be possible, we had to collect data from hundreds of research papers. The following page details all of the research papers in which we pulled data from. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[1] Chu, W., Lee, K., Song, S. et al. Review of biomimetic underwater robots using smart actuators. Int. J. Precis. Eng. Manuf. 13, 1281–1292 (2012). https://doi.org/10.1007/s12541-012-0171-7') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[2] J.M. Janie, M.Leary, Subic Aleksandar, Gibson, Mark A. "A review of shape memory allow research, applications and opportunities."') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[3] J. Ueda, T. W. Secord and H. H. Asada, "Large Effective-Strain Piezoelectric Actuators Using Nested Cellular Architecture With Exponential Strain Amplification Mechanisms," in IEEE/ASME Transactions on Mechatronics, vol. 15, no. 5, pp. 770-782, Oct. 2010. doi: 10.1109/TMECH.2009.2034973') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[4] P. A. York and R. J. Wood, "A geometrically-amplified in-plane piezoelectric actuator for mesoscale robotic systems," 2017 IEEE International Conference on Robotics and Automation (ICRA), Singapore, 2017, pp. 1263-1268, doi: 10.1109/ICRA.2017.7989150.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[5] Ron Pelrine, Roy Kornbluh, Qibing Pei, Jose Joseph. “High-Speed Electrically Actuated Elastomers with Strain Greater Than 100%”') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[6] Tadesse, Y., Thayer, N., & Priya, S. (2010). Tailoring the Response Time of Shape Memory Alloy Wires through Active Cooling and Pre-stress. Journal of Intelligent Material Systems and Structures, 21(1), 19–40. https://doi.org/10.1177/1045389X09352814') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[7] Kenneth Meijer, Marc S. Rosenthal, and Robert J. Full "Muscle-like actuators? A comparison between three electroactive polymers", Proc. SPIE 4329, Smart Structures and Materials 2001: Electroactive Polymer Actuators and Devices, (16 July 2001); doi: 10.1117/12.432649;https://doi.org/10.1117/12.432649') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[9] Mirvakili, S. M., Hunter, I. W., Adv. Mater. 2018, 30, 1704407. https://doi.org/10.1002/adma.201704407') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[11] Shahinpoor, Mohsen & Bar-Cohen, Yoseph & Simpson, J.O. & Smith, J. (1998). Ionic Polymer-Metal Composites (IPMCs) as Biomimetic Sensors, Actuators and Artificial Muscles: A Review. Smart Materials and Structures. 7. 10.1088/0964-1726/7/6/001. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[12] F. Daerden, D. Lefeber, B. Verrelst and R. Van Ham, "Pleated pneumatic artificial muscles: actuators for automation and robotics," 2001 IEEE/ASME International Conference on Advanced Intelligent Mechatronics. Proceedings (Cat. No.01TH8556), Como, Italy, 2001, pp. 738-743 vol.2.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[14] T. E. Pillsbury, Q. Guan and N. M. Wereley, "Comparison of contractile and extensile pneumatic artificial muscles," 2016 IEEE International Conference on Advanced Intelligent Mechatronics (AIM), Banff, AB, 2016, pp. 94-99.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[15] I. W. Hunter and S. Lafontaine, "A comparison of muscle with artificial actuators," Technical Digest IEEE Solid-State Sensor and Actuator Workshop, Hilton Head Island, SC, USA, 1992, pp. 178-185') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[17] K. Meijer, M. Rosenthal, and R.J. Full (2001)“Muscle-Like Actuators? A Comparison Between Three Electroactive Polymers.” Proc. SPIE 4329: 7-15') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[18] Pelrine, R., Kornbluh, R.D., Pei, Q., Stanford, S., Oh, S., Eckerle, J.S., Full, R.J., Rosenthal, M., & Meijer, K. (2002). Dielectric elastomer artificial muscle actuators: toward biomimetic motion.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[19] J. D. W. Madden et al., "Artificial muscle technology: physical principles and naval prospects," in IEEE Journal of Oceanic Engineering, vol. 29, no. 3, pp. 706-728, July 2004.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[20] B. Tondu, “Modelling of the McKibben artificial muscle: A review,” J. Intell. Mater. Syst. Struct., vol. 23, no. 3, pp. 225–253, 2012.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[21] Ashley, Steven. (2008). Artificial Muscles. Scientific American. 18. 53-59. 10.1038/scientificamerican0208-64sp.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[22]  Bar-Cohen, Yoseph. (2001). Electroactive Polymers as Artificial Muscles - Reality and Challenges. 19th AIAA Applied Aerodynamics Conference. 10.2514/6.2001-1492. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[23] S. I. Rich, R. J. Wood, and C. Majidi, “Untethered soft robotics,” Nature Electronics, vol. 1, no. 2, p. 102, 2018.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[27] R. J. Wood, B. Finio, M. Karpelson, K. Ma, N. O. Perez-Arancibia,  P. S. Sreetharan, H. Tanaka, and J. P. Whitney, “Progress on “pico” air vehicles,” Springer Tracts in Advanced Robotics, vol. 100, pp. 3–19, 2017.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[29] Duduta, Mihai & Hajiesmaili, Ehsan & Zhao, Huichan & Wood, Robert & Clarke, David. (2019). Realizing the potential of dielectric elastomer artificial muscles. Proceedings of the National Academy of Sciences. 116. 201815053. 10.1073/pnas.1815053116.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[31] Mohd Jani, J., Leary, M., & Subic, A. (2017). Designing shape memory alloy linear actuators: A review. Journal of Intelligent Material Systems and Structures, 28(13), 1699–1718. https://doi.org/10.1177/1045389X16679296') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[32] C. Liu, H. Qin, and P. Mather, “Review of progress in shape-memory polymers,” J. Mater. Chem., vol. 17, pp. 1543–1558, 2007.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[36] M. Usman, H. Seong, B. Suthar, I. Gaponov and J. Ryu, "A study on life cycle of twisted string actuators: Preliminary results," 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Vancouver, BC, 2017, pp. 4680-4685.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[37] Haines, Carter S. et al. “Artificial Muscles from Fishing Line and Sewing Thread.” Science 343 (2014): 868-872.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[38] M. C. Yip and G. Niemeyer, “On the control and properties of supercoiled polymer artificial muscles,” IEEE Trans. Robot., vol. 33, no. 3, pp. 689–699, 2017') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[40] R. Pelrine, R. Kornbluh, Q. Pei, S. Stanford, S. Oh, J. Eckerle, R. Full, M. Rosenthal, and K. Meijer, “Dielectric elastomer artificial muscle actuators: Toward biomimetic motion,” in Proc. SPIE Electroactive Polymer Actuators and Devices, vol. 4695, 2002') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[42] S. J. Kim, D. Pugal, J. Wong, K. J. Kim, and W. Yim, “A bio-inspired multi degree of freedom actuator based on a novel cylindrical ionic polymermetal composite material,” Robot. Auton. Syst., vol. 62, no. 1, pp. 53–60, 2014. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[47] G. Palli, C. Natale, C. May, C. Melchiorri, and T. Wurtz, “Modeling and control of the twisted string actuation system,” IEEE/ASME Trans. Mech., vol. 18, no. 2, pp. 664–673, 2013.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[49] J. Zhang, K. Iyer, A. Simeonov, and M. C. Yip, “Modeling and inverse compensation of hysteresis in super-coiled polymer artificial muscles,” IEEE Robot. Autom. Lett., vol. 2, no. 2, pp. 773–780, 2017.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[51] Ahmed, Saad & Ounaies, Zoubeida & Frecker, M. (2014). Investigating the performance and properties of dielectric elastomer actuators as a potential means to actuate origami structures. Smart Materials and Structures. 23. 094003. 10.1088/0964-1726/23/9/094003.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[52] Rossi, Claudio et al. “Bending continuous structures with SMAs: a novel robotic fish design.” Bioinspiration & biomimetics 6 4 (2011): 045005 .') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[53] Wu, Lianjun et al. “Compact and low-cost humanoid hand powered by nylon artificial muscles.” Bioinspiration & biomimetics 12 2 (2017): 026004 .') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[54] Small, Ward & Singhal, Pooja & Wilson, Thomas & Maitland, Duncan. (2010). Biomedical applications of thermally activated shape memory polymers. Journal of materials chemistry. 20. 3356-3366. 10.1039/B923717H. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[55] Lendlein, Andreas & Langer, Robert. (2002). Biodegradable, elastic shape-memory polymers for potential BIOMEDICAL applications. Science (New York, N.Y.). 296. 1673-6. 10.1126/science.1066102.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[57] Bar-Cohen, Yoseph & Xue, T & Shahinpoor, Mohsen & Simpson, J & Smith, J. (1998). Flexible, Low-mass Robotic Arm Actuated by Electroactive Polymers and Operated Equivalently to Human Arm and Hand. 10.1061/40337(205)3.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[58] Li, Jian & Sedaghati, Ramin & Dargahi, Javad. (2004). Design and Development of Piezoelectric Inchworm Actuator. Mechatronics. 15. 10.2514/6.2004-1890.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[59] Herr, Hugh & Kornbluh, Roy. (2004). New horizons for orthotic and prosthetic technology: Artificial muscle for ambulation. Proceedings of SPIE - The International Society for Optical Engineering. 5385. 10.1117/12.544510.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[60] J. McBean and C. Breazeal, "Voice coil actuators for human-robot interaction," 2004 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (IEEE Cat. No.04CH37566), Sendai, 2004, pp. 852-858 vol.1.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[77] Ayvali, Elif & Liang, Chia-Pin & Ho, Mingyen & Chen, Yu & P Desai, Jaydev. (2012). Towards A Discretely Actuated Steerable Cannula for Diagnostic and Therapeutic Procedures. The International journal of robotics research. 31. 588-603. 10.1177/0278364912442429. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[84] Wissler, Michael & Mazza, Edoardo. (2005). Modeling of a pre-strained circular actuator made of dielectric elastomers. Sensors and Actuators A-physical - SENSOR ACTUATOR A-PHYS. 120. 184-192. 10.1016/j.sna.2004.11.015. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[85] Sarban, Rahimullah & Jones, Richard & Mace, Brian & Rustighi, Emiliano. (2011). A tubular dielectric elastomer actuator: Fabrication, characterization and active vibration isolation. Mechanical Systems and Signal Processing - MECH SYST SIGNAL PROCESS. 25. 2879-2891. 10.1016/j.ymssp.2011.06.004.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[89]  M. Al Janaideh, S. Rakheja, and C.-Y. Su, “A generalized Prandtl–Ishlinskii model for characterizing the hysteresis and saturation nonlinearities of smart actuators,” Smart Mater. Struct., vol. 18, no. 4, p. 045001, Mar. 2009. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[94] C.-P. Chou and B. Hannaford, “Measurement and modeling of McKibben pneumatic artificial muscles,” IEEE Trans. Rob. Autom., vol. 12, no. 1, pp. 90–102, Feb. 1996.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[103] I. W. Hunter and S. Lafontaine, "A comparison of muscle with artificial actuators," Technical Digest IEEE Solid-State Sensor and Actuator Workshop, Hilton Head Island, SC, USA, 1992, pp. 178-185.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[104] J.M. Hollerbach, I.W. Hunter and J. Ballantyne,”A comparative analysis of actuator technologies for robotics”. https://groups.csail.mit.edu/drl/journal_club/papers/Hollerbach_Hunter_Ballantyne__1992__A_Comparative_Analysis_of_Actuator_Technologies_for_Robotics.pdf') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[105] Yoseph Bar-Cohen, “Electroactive Polymers as Artificial Muscles: Capabilities, potentials and Challenges”.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[106] Roy D. Kornbluh, Ron Pelrine, Qibing Pei, Seajin Oh, Jose Joseph, "Ultrahigh strain response of field-actuated elastomeric polymers," Proc. SPIE 3987, Smart Structures and Materials 2000: Electroactive Polymer Actuators and Devices (EAPAD), (7 June 2000);') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[108] Mohammed Benslimane, Peter Gravesen, Peter Sommer-Larsen, "Mechanical properties of dielectric elastomer actuators with smart metallic compliant electrodes," Proc. SPIE 4695, Smart Structures and Materials 2002: Electroactive Polymer Actuators and Devices (EAPAD), (11 July 2002);') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[113] Steven G. Wax, Randall R. Sands, "Electroactive polymer actuators and devices," Proc. SPIE 3669, Smart Structures and Materials 1999: Electroactive Polymer Actuators and Devices, (28 May 1999);') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[114] Robert J. Full, Kenneth Meijer, "Artificial muscles versus natural actuators from frogs to flies," Proc. SPIE 3987, Smart Structures and Materials 2000: Electroactive Polymer Actuators and Devices (EAPAD), (7 June 2000)') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[116] Yoseph Bar-Cohen, Cynthia Breazeal, "Biologically inspired intelligent robots," Proc. SPIE 5051, Smart Structures and Materials 2003: Electroactive Polymer Actuators and Devices (EAPAD), (28 July 2003);') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[117] M. Colli, A. Bellini, C. Concari, A. Toscani and G. Franceschini, "Current-Controlled Shape Memory Alloy Actuators for Automotive Tumble Flap," IECON 2006 - 32nd Annual Conference on IEEE Industrial Electronics, Paris, 2006, pp. 3987-3990.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[118] Awad Khidir Elwaleed, Nik Abdullah Mohamed, Mohd Jailani Mohd Nor, Mohd Marzuki Mustafa, “A new concept of a linear smart actuator,Sensors and Actuators A: Physical”,Volume 135, Issue 1,2007,Pages 244-249,ISSN 0924-4247, https://doi.org/10.1016/j.sna.2006.07.010. (http://www.sciencedirect.com/science/article/pii/S0924424706005048)') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[119] Shigeo Hirose, Koji Ikuta & Koichi Sato (1988) Development of a shape memory alloy actuator. Improvement of output performance by the introduction of a σ-mechanism, Advanced Robotics, 3:2, 89-108, DOI: 10.1163/156855389X00019') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[120] Kim, Hongjip et al. “Sensorless displacement estimation of a shape memory alloy coil spring actuator using inductance.” (2013).') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[121] W. Huang,On the selection of shape memory alloys for actuators,Materials & Design,Volume 23,Issue 1,2002,Pages 11-19,ISSN 0261-3069,https://doi.org/10.1016/S0261-3069(01)00039-5.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[122] Ikuta, Koji et al. “Shape memory alloy servo actuator system with electric resistance feedback and application for active endoscope.” Proceedings. 1988 IEEE International Conference on Robotics and Automation (1988): 427-430 vol.1.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[123] Jun, Hyoung Yoll. “Development of a fuel-powered compact SMA (Shape Memory Alloy) actuator system.” (2005).') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[124] Kuribayashi, K., 1986, “A New Actuator of a Joint Mechanism Using TiNi Alloy Wire,” Int. J. Robot. Res., 4, No. 4, pp. 47–58.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[125] Kuribayashi, Katsutoshi. “Improvement of the Response of an SMA Actuator Using a Temperature Sensor.” I. J. Robotics Res. 10 (1991): 13-20.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[126] Langbein, Sven & Czechowicz, Alexander. (2012). Adaptive Resetting of SMA-Actuators. Journal of Intelligent Material Systems and Structures - J INTEL MAT SYST STRUCT. 23. 127-134. 10.1177/1045389X11431741.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[127] Lara-Quintanilla, A. & Bersee, H.E.N. Shap. Mem. Superelasticity (2015) 1: 460. https://doi.org/10.1007/s40830-015-0038-8') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[128] M. Leary, S. Huang, T. Ataalla, A. Baxter, A. Subic,Design of shape memory alloy actuators for direct power by an automotive battery,Materials & Design,Volume 43,2013,Pages 460-466,ISSN 0261-3069,https://doi.org/10.1016/j.matdes.2012.07.002.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[129] Ma, Ning & Song, Gangbing. (2003). Control of shape memory alloy actuator using Pulse Width (PW) modulation. Smart Materials and Structures. 12. 712. 10.1088/0964-1726/12/5/007. ') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[130] Mertmann, M. & Vergani, G. Eur. Phys. J. Spec. Top. (2008) 158: 221.https://doi.org/10.1140/epjst/e2008-00679-9') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[131] Jani, J.M., Huang, S., Leary, M. et al. Comput Mech (2015) 56: 443. https://doi.org/10.1007/s00466-015-1180-z') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[132] Dominiek Reynaerts, Hendrik Van Brussel,Design aspects of shape memory actuators,Mechatronics,Volume 8, Issue 6,1998,Pages 635-656,ISSN 0957-4158,https://doi.org/10.1016/S0957-4158(98)00023-3.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[133] Dieter Stoeckel,The Shape Memory Effect--Phenomenon,Alloys and Applications.Proceedings: Shape Memory Alloys fo Power Systems EPRI   pp 1‐13') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[134] R. Velazquez, E. Pissaloux, J. Szewczyk and M. Hafez, "Miniature Shape Memory Alloy Actuator for Tactile Binary Information Display," Proceedings of the 2005 IEEE International Conference on Robotics and Automation, Barcelona, Spain, 2005, pp. 1344-1349. doi: 10.1109/ROBOT.2005.1570302') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[135] Vollach, S., Shilo, D. & Shlagman, H. Exp Mech (2016) 56: 1465. https://doi.org/10.1007/s11340-016-0172-z') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[136] Williams, Eric and Mohammad Elahinia. “An Automotive SMA Mirror Actuator: Modeling, Design, and Experimental Evaluation.” (2008).') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[137] Hugh M. Herr, Roy D. Kornbluh, "New horizons for orthotic and prosthetic technology: artificial muscle for ambulation," Proc. SPIE 5385, Smart Structures and Materials 2004: Electroactive Polymer Actuators and Devices (EAPAD), (27 July 2004);') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[138] R.H. Baughman,Conducting polymer artificial muscles,Synthetic Metals,Volume 78, Issue 3,1996,Pages 339-353,ISSN 0379-6779, https://doi.org/10.1016/0379-6779(96)80158-5.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[139] Smith, Colin et al. “Working principle of bio-inspired shape memory alloy composite actuators.” (2011).') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[140] Rodrigue, H., Wang, W., Bhandari, B. et al. Int. J. of Precis. Eng. and Manuf.-Green Tech. (2014) 1: 153. https://doi.org/10.1007/s40684-014-0020-5') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[141] Seelecke , S., and Mu¨ller , I. (February 10, 2004). "Shape memory alloy actuators in smart structures: Modeling and simulation ." ASME. Appl. Mech. Rev. January 2004; 57(1): 23–46. https://doi.org/10.1115/1.1584064') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[142] Liang, C., and Rogers, C. A. (January 1, 1993). "Design of Shape Memory Alloy Springs With Applications in Vibration Control." ASME. J. Vib. Acoust. January 1993; 115(1): 129–135.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[144] Byungkyu Kim, Moon Gu Lee, Young Pyo Lee, YongIn Kim, GeunHo Lee, An earthworm-like micro robot using shape memory alloy actuator,Sensors and Actuators A: Physical,Volume 125, Issue 2,2006,Pages 429-437, ISSN 0924-4247,https://doi.org/10.1016/j.sna.2005.05.004.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[145] Zhenlong Wang, Guanrong Hang, Jian Li, Yangwei Wang, Kai Xiao, A micro-robot fish with embedded SMA wire actuated flexible biomimetic fin,Sensors and Actuators A: Physical,Volume 144, Issue 2,2008,Pages 354-360,ISSN 0924-4247, https://doi.org/10.1016/j.sna.2008.02.013.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[146] Yonas Tadesse, "Electroactive polymer and shape memory alloy actuators in biomimetics and humanoids," Proc. SPIE 8687, Electroactive Polymer Actuators and Devices (EAPAD) 2013, 868709 (9 April 2013);') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[147] Tiwari, R & Garcia, E. (2011). The state of understanding of ionic polymer metal composite architecture: A review. Smart Materials and Structures. 20. 083001. 10.1088/0964-1726/20/8/083001.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[148] Bar-Cohen, Yoseph. (2000). Electroactive Polymers as Artificial Muscles-Capabilities, Potentials and Challenges. Handbook on Biomimetics. 11. 10.1061/40476(299)24.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[149] Shahinpoor, Mohsen & Bar-Cohen, Yoseph & Simpson, J.O. & Smith, J.. (1998). Ionic Polymer-Metal Composites (IPMCs) as Biomimetic Sensors, Actuators and Artificial Muscles: A Review. Smart Materials and Structures. 7. 10.1088/0964-1726/7/6/001.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[150] M. Yamakita, A. Sera, N. Kamamichi, K. Asaka and Zhi-Wei Luo, "Integrated design of IPMC actuator/sensor," Proceedings 2006 IEEE International Conference on Robotics and Automation, 2006. ICRA 2006., Orlando, FL, 2006, pp. 1834-1839. doi: 10.1109/ROBOT.2006.1641973') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[151] Yim, Woosoon & Lee, Joonsoo & Kim, Kwang. (2007). An artificial muscle actuator for biomimetic underwater propulsors. Bioinspiration & biomimetics. 2. S31-41. 10.1088/1748-3182/2/2/S04.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[153] Pelrine, Ron et al. “High-Strain Actuator Materials Based on Dielectric Elastomers.” (2000).') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[154] Chen, Zheng and Tan, Xiaobao. “A Control-oriented and Physics-Based Model for Ionic Polymer--Metal Composite Actuators.” IEEE/ASME Transactions on Mechatronics. 2008. 10.1109/TMECH.2008.920021') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[159] A. Nespoli, S. Besseghini, S. Pittaccio, E. Villa, S. Viscuso, "The high potential of shape memory alloys in developing miniature mechanical devices: A review on shape memory alloy mini-actuators", Sensors Actuators A Phys., vol. 158, no. 1, pp. 149-160, 2010.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[169] T. Zsurzsan, M. A. E. Andersen, Z. Zhang and N. A. Andersen, "Preisach model of hysteresis for the Piezoelectric Actuator Drive," IECON 2015 - 41st Annual Conference of the IEEE Industrial Electronics Society, Yokohama, 2015, pp. 002788-002793. doi: 10.1109/IECON.2015.7392524') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[170] B. Ru-bing and L. Xiao-xu, "Research on SMA Actuator," 2010 International Conference on Computational and Information Sciences, Chengdu, 2010, pp. 1336-1340.  doi: 10.1109/ICCIS.2010.352') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[171] Z. Shi, J. Tian, R. Luo, G. Zhao and T. Wang, "Multifeedback Control of a Shape Memory Alloy Actuator and a Trial Application," in IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 48, no. 7, pp. 1106-1119, July 2018. doi: 10.1109/TSMC.2016.2641465') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[173] Furst, Stephen J., John H. Crews, and Stefan Seelecke. "Stress, strain, and resistance behavior of two opposing shape memory alloy actuator wires for resistance-based self-sensing applications." Journal of Intelligent Material Systems and Structures 24.16 (2013): 1951-1968.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[176] Sahu, R. K., et al. “Stress-Strain Behaviour of Dielectric Elastomer for Actuators.” Applied Mechanics and Materials, vol. 789–790, Trans Tech Publications, Ltd., Sept. 2015, pp. 837–841. Crossref, doi:10.4028/www.scientific.net/amm.789-790.837.') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[180] Ravi Shankar,ac Tushar K. Ghoshcd and Richard J. Spontak. Dielectric elastomers as next-generation polymeric actuators. DOI: 10.1039/b705737g') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[182] Ailish O’Hallorana), Fergal O’Malley, and Peter McHugh. A review on dielectric elastomer actuators, technology, applications, and challenges. Journal of Applied Physics 104, 071101 (2008); https://doi.org/10.1063/1.2981642') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[183] A strain amplifying piezoelectric MEMS actuator. Nicholas J Conway, Zachary J Traina and Sang-Gook Kim. Published 9 March 2007 • 2007 IOP Publishing Ltd. Journal of Micromechanics and Microengineering, Volume 17, Number 4') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[185] N. Navapan-Traiphol, R. W. Schwartz, D. Stutts and J. Wood, "Characterization and modeling of local electromechanical response in stress-biased piezoelectric actuators," 14th IEEE International Symposium on Applications of Ferroelectrics, 2004. ISAF-04. 2004, Montreal, Que., Canada, 2004, pp. 56-59. doi: 10.1109/ISAF.2004.1418336') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[186] S. Yagnamurthy, I. Chasiotis, “ Mechanical and Piezoelectric Behavior of Thin Film PZT Composites for MEMS Applications” Proceedings of the SEM Annual Conference, 2010. https://link.springer.com/content/pdf/10.1007%2F978-1-4419-8825-6_37.pdf') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[188] G. Lau, T. La and D. Di-Teng Tan, "High-stress dielectric elastomer actuators with oil encapsulation," 2014 11th International Conference on Ubiquitous Robots and Ambient Intelligence (URAI), Kuala Lumpur, 2014, pp. 196-197. doi: 10.1109/URAI.2014.7057530') 
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='[189] Runan Zhang, Pejman Iravani, Patrick Keogh, “Effects of Off-Plane Deformation and Biased Bi-Axial Pre-Strains on a Planar Contractile Dielectric Elastomer Actuator” Actuators 2018, 7(4), 75; https://doi.org/10.3390/act7040075') 
                    , className="mb-4")
        ]),
    ])
])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)