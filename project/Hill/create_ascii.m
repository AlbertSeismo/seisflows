load('./foothill.mat');
mkdir('./model_true');
mkdir('./model_init');
NPROC = 2;
%%
dx = 5;
rho = 2500;
vs = 1000;
vp0 = 5000;
vp = vpfinalnew(:,:,10);
F = griddedInterpolant(vp);
%imagesc(vpfinalnew(:,:,1))
for PROC = 1:NPROC
    homo = load(['./model/proc',num2str(PROC-1,'%06d'),'_rho_vp_vs.dat']);
    homo(:,5) = vs;
    save(['./model_init/proc',num2str(PROC-1,'%06d'),'_rho_vp_vs.dat'],'homo','-ascii')
    for i = 1:length(homo)
        homo(i,4) = F(50-(homo(i,2)/dx+1), homo(i,1)/dx + 1);
    end

    

    save(['./model_true/proc',num2str(PROC-1,'%06d'),'_rho_vp_vs.dat'],'homo','-ascii')
    %clear homo
end

