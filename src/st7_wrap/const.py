"""Some curated enum types auto-generated from St7API.py by _constants_generate.py"""

import enum

import St7API


__all__ = [
    "AttributeType",
    "BeamContour",
    "BrickContour",
    "Entity",
    "GlobalInteger",
    "ImageType",
    "NodeResultType",
    "PlateContour",
    "PlateResultSubType",
    "PlateResultType",
    "PlateSurface",
    "PreLoadType",
    "Property",
    "SampleLocation",
    "ScaleType",
    "SolverDefaultInteger",
    "SolverDefaultLogical",
    "SolverMode",
    "SolverType",
    "TableType",
    "WindowsRefreshMode",
]


class AttributeType(enum.Enum):
    aoRestraint = St7API.aoRestraint
    aoForce = St7API.aoForce
    aoMoment = St7API.aoMoment
    aoTemperature = St7API.aoTemperature
    aoMTranslation = St7API.aoMTranslation
    aoMRotation = St7API.aoMRotation
    aoKTranslation = St7API.aoKTranslation
    aoKRotation = St7API.aoKRotation
    aoDamping = St7API.aoDamping
    aoNSMass = St7API.aoNSMass
    aoNodeInfluence = St7API.aoNodeInfluence
    aoNodeHeatSource = St7API.aoNodeHeatSource
    aoNodeVelocity = St7API.aoNodeVelocity
    aoNodeAcceleration = St7API.aoNodeAcceleration
    aoVertexMeshSize = St7API.aoVertexMeshSize


class BeamContour(enum.Enum):
    ctBeamNone = St7API.ctBeamNone
    ctBeamLength = St7API.ctBeamLength
    ctBeamAxis1 = St7API.ctBeamAxis1
    ctBeamAxis2 = St7API.ctBeamAxis2
    ctBeamAxis3 = St7API.ctBeamAxis3
    ctBeamEA = St7API.ctBeamEA
    ctBeamEI11 = St7API.ctBeamEI11
    ctBeamEI22 = St7API.ctBeamEI22
    ctBeamGJ = St7API.ctBeamGJ
    ctBeamEAFactor = St7API.ctBeamEAFactor
    ctBeamEI11Factor = St7API.ctBeamEI11Factor
    ctBeamEI22Factor = St7API.ctBeamEI22Factor
    ctBeamGJFactor = St7API.ctBeamGJFactor
    ctBeamOffset1 = St7API.ctBeamOffset1
    ctBeamOffset2 = St7API.ctBeamOffset2
    ctBeamStiffnessFactor1 = St7API.ctBeamStiffnessFactor1
    ctBeamStiffnessFactor2 = St7API.ctBeamStiffnessFactor2
    ctBeamStiffnessFactor3 = St7API.ctBeamStiffnessFactor3
    ctBeamStiffnessFactor4 = St7API.ctBeamStiffnessFactor4
    ctBeamStiffnessFactor5 = St7API.ctBeamStiffnessFactor5
    ctBeamStiffnessFactor6 = St7API.ctBeamStiffnessFactor6
    ctBeamMassFactor = St7API.ctBeamMassFactor
    ctBeamSupportM1 = St7API.ctBeamSupportM1
    ctBeamSupportP1 = St7API.ctBeamSupportP1
    ctBeamSupportM2 = St7API.ctBeamSupportM2
    ctBeamSupportP2 = St7API.ctBeamSupportP2
    ctBeamSupportGapM1 = St7API.ctBeamSupportGapM1
    ctBeamSupportGapP1 = St7API.ctBeamSupportGapP1
    ctBeamSupportGapM2 = St7API.ctBeamSupportGapM2
    ctBeamSupportGapP2 = St7API.ctBeamSupportGapP2
    ctBeamTemperature = St7API.ctBeamTemperature
    ctBeamTempGradient1 = St7API.ctBeamTempGradient1
    ctBeamTempGradient2 = St7API.ctBeamTempGradient2
    ctBeamPreTension = St7API.ctBeamPreTension
    ctBeamPreStrain = St7API.ctBeamPreStrain
    ctBeamPreCurvature1 = St7API.ctBeamPreCurvature1
    ctBeamPreCurvature2 = St7API.ctBeamPreCurvature2
    ctBeamPipePressureIn = St7API.ctBeamPipePressureIn
    ctBeamPipePressureOut = St7API.ctBeamPipePressureOut
    ctBeamPipeTempIn = St7API.ctBeamPipeTempIn
    ctBeamPipeTempOut = St7API.ctBeamPipeTempOut
    ctBeamConvectionCoeff = St7API.ctBeamConvectionCoeff
    ctBeamConvectionAmbient = St7API.ctBeamConvectionAmbient
    ctBeamRadiationCoeff = St7API.ctBeamRadiationCoeff
    ctBeamRadiationAmbient = St7API.ctBeamRadiationAmbient
    ctBeamHeatFlux = St7API.ctBeamHeatFlux
    ctBeamHeatSource = St7API.ctBeamHeatSource
    ctBeamAgeAtFirstLoading = St7API.ctBeamAgeAtFirstLoading


class BrickContour(enum.Enum):
    ctBrickNone = St7API.ctBrickNone
    ctBrickAspectRatioMin = St7API.ctBrickAspectRatioMin
    ctBrickAspectRatioMax = St7API.ctBrickAspectRatioMax
    ctBrickDeterminant = St7API.ctBrickDeterminant
    ctBrickInternalAngle = St7API.ctBrickInternalAngle
    ctBrickMixedProduct = St7API.ctBrickMixedProduct
    ctBrickDihedral = St7API.ctBrickDihedral
    ctBrickVolume = St7API.ctBrickVolume
    ctBrickAxis1 = St7API.ctBrickAxis1
    ctBrickAxis2 = St7API.ctBrickAxis2
    ctBrickAxis3 = St7API.ctBrickAxis3
    ctBrickNormalSupport = St7API.ctBrickNormalSupport
    ctBrickLateralSupport = St7API.ctBrickLateralSupport
    ctBrickSupportGap = St7API.ctBrickSupportGap
    ctBrickTemperature = St7API.ctBrickTemperature
    ctBrickPreStressX = St7API.ctBrickPreStressX
    ctBrickPreStressY = St7API.ctBrickPreStressY
    ctBrickPreStressZ = St7API.ctBrickPreStressZ
    ctBrickPreStressMagnitude = St7API.ctBrickPreStressMagnitude
    ctBrickPreStrainX = St7API.ctBrickPreStrainX
    ctBrickPreStrainY = St7API.ctBrickPreStrainY
    ctBrickPreStrainZ = St7API.ctBrickPreStrainZ
    ctBrickPreStrainMagnitude = St7API.ctBrickPreStrainMagnitude
    ctBrickNormalPressure = St7API.ctBrickNormalPressure
    ctBrickGlobalPressureX = St7API.ctBrickGlobalPressureX
    ctBrickGlobalPressureY = St7API.ctBrickGlobalPressureY
    ctBrickGlobalPressureZ = St7API.ctBrickGlobalPressureZ
    ctBrickGlobalPressureMagnitude = St7API.ctBrickGlobalPressureMagnitude
    ctBrickShearX = St7API.ctBrickShearX
    ctBrickShearY = St7API.ctBrickShearY
    ctBrickShearMagnitude = St7API.ctBrickShearMagnitude
    ctBrickNSMass = St7API.ctBrickNSMass
    ctBrickDynamicFactor = St7API.ctBrickDynamicFactor
    ctBrickConvectionCoeff = St7API.ctBrickConvectionCoeff
    ctBrickConvectionAmbient = St7API.ctBrickConvectionAmbient
    ctBrickRadiationCoeff = St7API.ctBrickRadiationCoeff
    ctBrickRadiationAmbient = St7API.ctBrickRadiationAmbient
    ctBrickHeatFlux = St7API.ctBrickHeatFlux
    ctBrickHeatSource = St7API.ctBrickHeatSource
    ctBrickSoilStressSV = St7API.ctBrickSoilStressSV
    ctBrickSoilStressK0 = St7API.ctBrickSoilStressK0
    ctBrickSoilStressSH = St7API.ctBrickSoilStressSH
    ctBrickSoilRatioOCR = St7API.ctBrickSoilRatioOCR
    ctBrickSoilRatioE0 = St7API.ctBrickSoilRatioE0
    ctBrickSoilFluidLevel = St7API.ctBrickSoilFluidLevel
    ctBrickAgeAtFirstLoading = St7API.ctBrickAgeAtFirstLoading


class Entity(enum.Enum):
    tyNODE = St7API.tyNODE
    tyBEAM = St7API.tyBEAM
    tyPLATE = St7API.tyPLATE
    tyBRICK = St7API.tyBRICK
    tyLINK = St7API.tyLINK
    tyVERTEX = St7API.tyVERTEX
    tyGEOMETRYEDGE = St7API.tyGEOMETRYEDGE
    tyGEOMETRYFACE = St7API.tyGEOMETRYFACE
    tyLOADPATH = St7API.tyLOADPATH
    tyGEOMETRYCOEDGE = St7API.tyGEOMETRYCOEDGE
    tyGEOMETRYLOOP = St7API.tyGEOMETRYLOOP


class GlobalInteger(enum.Enum):
    ivTessellationsFailed = St7API.ivTessellationsFailed
    ivSeamsAdded = St7API.ivSeamsAdded
    ivIntersectionsFound = St7API.ivIntersectionsFound
    ivPlateEdgesAssigned = St7API.ivPlateEdgesAssigned
    ivPlateEdgesNotFullyAssigned = St7API.ivPlateEdgesNotFullyAssigned
    ivAttachmentsCreated = St7API.ivAttachmentsCreated
    ivAttachmentsFailed = St7API.ivAttachmentsFailed
    ivNodesCreated = St7API.ivNodesCreated
    ivNodesDeleted = St7API.ivNodesDeleted
    ivNodesMoved = St7API.ivNodesMoved
    ivBeamsChanged = St7API.ivBeamsChanged
    ivBeamsCollapsed = St7API.ivBeamsCollapsed
    ivBeamsCreated = St7API.ivBeamsCreated
    ivBeamsDeleted = St7API.ivBeamsDeleted
    ivBeamsFailed = St7API.ivBeamsFailed
    ivBeamsMoved = St7API.ivBeamsMoved
    ivBeamsSplit = St7API.ivBeamsSplit
    ivBeamsSubdivided = St7API.ivBeamsSubdivided
    ivPlatesChanged = St7API.ivPlatesChanged
    ivPlatesCollapsed = St7API.ivPlatesCollapsed
    ivPlatesCreated = St7API.ivPlatesCreated
    ivPlatesDeleted = St7API.ivPlatesDeleted
    ivPlatesFailed = St7API.ivPlatesFailed
    ivPlatesGraded = St7API.ivPlatesGraded
    ivPlatesMoved = St7API.ivPlatesMoved
    ivPlatesSplit = St7API.ivPlatesSplit
    ivPlatesSubdivided = St7API.ivPlatesSubdivided
    ivBricksChanged = St7API.ivBricksChanged
    ivBricksCollapsed = St7API.ivBricksCollapsed
    ivBricksCreated = St7API.ivBricksCreated
    ivBricksDeleted = St7API.ivBricksDeleted
    ivBricksFailed = St7API.ivBricksFailed
    ivBricksGraded = St7API.ivBricksGraded
    ivBricksMoved = St7API.ivBricksMoved
    ivBricksSplit = St7API.ivBricksSplit
    ivBricksSubdivided = St7API.ivBricksSubdivided
    ivLinksChanged = St7API.ivLinksChanged
    ivLinksCollapsed = St7API.ivLinksCollapsed
    ivLinksCreated = St7API.ivLinksCreated
    ivLinksDeleted = St7API.ivLinksDeleted
    ivLinksMoved = St7API.ivLinksMoved
    ivLoadPathsChanged = St7API.ivLoadPathsChanged
    ivLoadPathsCreated = St7API.ivLoadPathsCreated
    ivLoadPathsMoved = St7API.ivLoadPathsMoved
    ivFacesChanged = St7API.ivFacesChanged
    ivFacesCreated = St7API.ivFacesCreated
    ivFacesDeleted = St7API.ivFacesDeleted
    ivFacesFailed = St7API.ivFacesFailed
    ivFacesMoved = St7API.ivFacesMoved
    ivEdgesMorphed = St7API.ivEdgesMorphed
    ivEdgesSubdivided = St7API.ivEdgesSubdivided
    ivLoopsDeleted = St7API.ivLoopsDeleted
    ivAttributesApplied = St7API.ivAttributesApplied
    ivUCSCreated = St7API.ivUCSCreated
    ivPatchPlatesCreated = St7API.ivPatchPlatesCreated
    ivLoadCasesCreated = St7API.ivLoadCasesCreated
    ivFilletsCreated = St7API.ivFilletsCreated
    ivFilletsFailed = St7API.ivFilletsFailed
    ivLoftSeriesFound = St7API.ivLoftSeriesFound
    ivDuplicateBeamsDeleted = St7API.ivDuplicateBeamsDeleted
    ivDuplicatePlatesDeleted = St7API.ivDuplicatePlatesDeleted
    ivDuplicateBricksDeleted = St7API.ivDuplicateBricksDeleted
    ivDuplicateLinksDeleted = St7API.ivDuplicateLinksDeleted
    ivStringGroupsPacked = St7API.ivStringGroupsPacked
    ivClipboardNodes = St7API.ivClipboardNodes
    ivClipboardBeams = St7API.ivClipboardBeams
    ivClipboardPlates = St7API.ivClipboardPlates
    ivClipboardBricks = St7API.ivClipboardBricks
    ivClipboardLinks = St7API.ivClipboardLinks
    ivClipboardLoadPaths = St7API.ivClipboardLoadPaths
    ivClipboardFaces = St7API.ivClipboardFaces
    ivClipboardVertices = St7API.ivClipboardVertices
    ivFacesMeshed = St7API.ivFacesMeshed
    ivFacesPartiallyMeshed = St7API.ivFacesPartiallyMeshed
    ivFacesNotMeshed = St7API.ivFacesNotMeshed
    ivSolverTerminationCode = St7API.ivSolverTerminationCode
    ivSolidsMeshed = St7API.ivSolidsMeshed
    ivSolidsPartiallyMeshed = St7API.ivSolidsPartiallyMeshed
    ivSolidsNotMeshed = St7API.ivSolidsNotMeshed


class ImageType(enum.Enum):
    itBitmap8Bit = St7API.itBitmap8Bit
    itBitmap16Bit = St7API.itBitmap16Bit
    itBitmap24Bit = St7API.itBitmap24Bit
    itJPEG = St7API.itJPEG
    itPNG = St7API.itPNG


class NodeResultType(enum.Enum):
    rtNodeDisp = St7API.rtNodeDisp
    rtNodeVel = St7API.rtNodeVel
    rtNodeAcc = St7API.rtNodeAcc
    rtNodePhase = St7API.rtNodePhase
    rtNodeReact = St7API.rtNodeReact
    rtNodeTemp = St7API.rtNodeTemp
    rtNodeFlux = St7API.rtNodeFlux
    rtNodeInertia = St7API.rtNodeInertia
    rtNodeInfluence = St7API.rtNodeInfluence


class PlateContour(enum.Enum):
    ctPlateNone = St7API.ctPlateNone
    ctPlateAspectRatioMin = St7API.ctPlateAspectRatioMin
    ctPlateAspectRatioMax = St7API.ctPlateAspectRatioMax
    ctPlateWarping = St7API.ctPlateWarping
    ctPlateInternalAngle = St7API.ctPlateInternalAngle
    ctPlateInternalAngleRatio = St7API.ctPlateInternalAngleRatio
    ctPlateArea = St7API.ctPlateArea
    ctPlateAxis1 = St7API.ctPlateAxis1
    ctPlateAxis2 = St7API.ctPlateAxis2
    ctPlateAxis3 = St7API.ctPlateAxis3
    ctPlateDiscreteThicknessM = St7API.ctPlateDiscreteThicknessM
    ctPlateContinuousThicknessM = St7API.ctPlateContinuousThicknessM
    ctPlateDiscreteThicknessB = St7API.ctPlateDiscreteThicknessB
    ctPlateContinuousThicknessB = St7API.ctPlateContinuousThicknessB
    ctPlateOffset = St7API.ctPlateOffset
    ctPlateStiffnessFactor1 = St7API.ctPlateStiffnessFactor1
    ctPlateStiffnessFactor2 = St7API.ctPlateStiffnessFactor2
    ctPlateStiffnessFactor3 = St7API.ctPlateStiffnessFactor3
    ctPlateStiffnessFactor4 = St7API.ctPlateStiffnessFactor4
    ctPlateStiffnessFactor5 = St7API.ctPlateStiffnessFactor5
    ctPlateStiffnessFactor6 = St7API.ctPlateStiffnessFactor6
    ctPlateStiffnessFactor7 = St7API.ctPlateStiffnessFactor7
    ctPlateStiffnessFactor8 = St7API.ctPlateStiffnessFactor8
    ctPlateStiffnessFactor9 = St7API.ctPlateStiffnessFactor9
    ctPlateMassFactor = St7API.ctPlateMassFactor
    ctPlateEdgeNormalSupport = St7API.ctPlateEdgeNormalSupport
    ctPlateEdgeLateralSupport = St7API.ctPlateEdgeLateralSupport
    ctPlateEdgeSupportGap = St7API.ctPlateEdgeSupportGap
    ctPlateFaceNormalSupportMinusZ = St7API.ctPlateFaceNormalSupportMinusZ
    ctPlateFaceNormalSupportPlusZ = St7API.ctPlateFaceNormalSupportPlusZ
    ctPlateFaceLateralSupportMinusZ = St7API.ctPlateFaceLateralSupportMinusZ
    ctPlateFaceLateralSupportPlusZ = St7API.ctPlateFaceLateralSupportPlusZ
    ctPlateFaceSupportGapMinusZ = St7API.ctPlateFaceSupportGapMinusZ
    ctPlateFaceSupportGapPlusZ = St7API.ctPlateFaceSupportGapPlusZ
    ctPlateTemperature = St7API.ctPlateTemperature
    ctPlateTempGradient = St7API.ctPlateTempGradient
    ctPlatePreStressX = St7API.ctPlatePreStressX
    ctPlatePreStressY = St7API.ctPlatePreStressY
    ctPlatePreStressZ = St7API.ctPlatePreStressZ
    ctPlatePreStressMagnitude = St7API.ctPlatePreStressMagnitude
    ctPlatePreStrainX = St7API.ctPlatePreStrainX
    ctPlatePreStrainY = St7API.ctPlatePreStrainY
    ctPlatePreStrainZ = St7API.ctPlatePreStrainZ
    ctPlatePreStrainMagnitude = St7API.ctPlatePreStrainMagnitude
    ctPlatePreCurvatureX = St7API.ctPlatePreCurvatureX
    ctPlatePreCurvatureY = St7API.ctPlatePreCurvatureY
    ctPlatePreCurvatureMagnitude = St7API.ctPlatePreCurvatureMagnitude
    ctPlateEdgeNormalPressure = St7API.ctPlateEdgeNormalPressure
    ctPlateEdgeShear = St7API.ctPlateEdgeShear
    ctPlateEdgeTransverseShear = St7API.ctPlateEdgeTransverseShear
    ctPlateEdgeGlobalPressureX = St7API.ctPlateEdgeGlobalPressureX
    ctPlateEdgeGlobalPressureY = St7API.ctPlateEdgeGlobalPressureY
    ctPlateEdgeGlobalPressureZ = St7API.ctPlateEdgeGlobalPressureZ
    ctPlateEdgeGlobalPressure = St7API.ctPlateEdgeGlobalPressure
    ctPlateNormalPressureMinusZ = St7API.ctPlateNormalPressureMinusZ
    ctPlateNormalPressurePlusZ = St7API.ctPlateNormalPressurePlusZ
    ctPlateGlobalPressureXMinusZ = St7API.ctPlateGlobalPressureXMinusZ
    ctPlateGlobalPressureYMinusZ = St7API.ctPlateGlobalPressureYMinusZ
    ctPlateGlobalPressureZMinusZ = St7API.ctPlateGlobalPressureZMinusZ
    ctPlateGlobalPressureMinusZ = St7API.ctPlateGlobalPressureMinusZ
    ctPlateGlobalPressureXPlusZ = St7API.ctPlateGlobalPressureXPlusZ
    ctPlateGlobalPressureYPlusZ = St7API.ctPlateGlobalPressureYPlusZ
    ctPlateGlobalPressureZPlusZ = St7API.ctPlateGlobalPressureZPlusZ
    ctPlateGlobalPressurePlusZ = St7API.ctPlateGlobalPressurePlusZ
    ctPlateFaceShearX = St7API.ctPlateFaceShearX
    ctPlateFaceShearY = St7API.ctPlateFaceShearY
    ctPlateFaceShearMagnitude = St7API.ctPlateFaceShearMagnitude
    ctPlateNSMass = St7API.ctPlateNSMass
    ctPlateDynamicFactor = St7API.ctPlateDynamicFactor
    ctPlateConvectionCoeff = St7API.ctPlateConvectionCoeff
    ctPlateConvectionAmbient = St7API.ctPlateConvectionAmbient
    ctPlateRadiationCoeff = St7API.ctPlateRadiationCoeff
    ctPlateRadiationAmbient = St7API.ctPlateRadiationAmbient
    ctPlateHeatFlux = St7API.ctPlateHeatFlux
    ctPlateConvectionCoeffPlusZ = St7API.ctPlateConvectionCoeffPlusZ
    ctPlateConvectionCoeffMinusZ = St7API.ctPlateConvectionCoeffMinusZ
    ctPlateConvectionAmbientPlusZ = St7API.ctPlateConvectionAmbientPlusZ
    ctPlateConvectionAmbientMinusZ = St7API.ctPlateConvectionAmbientMinusZ
    ctPlateRadiationCoeffPlusZ = St7API.ctPlateRadiationCoeffPlusZ
    ctPlateRadiationCoeffMinusZ = St7API.ctPlateRadiationCoeffMinusZ
    ctPlateRadiationAmbientPlusZ = St7API.ctPlateRadiationAmbientPlusZ
    ctPlateRadiationAmbientMinusZ = St7API.ctPlateRadiationAmbientMinusZ
    ctPlateHeatSource = St7API.ctPlateHeatSource
    ctPlateSoilStressSV = St7API.ctPlateSoilStressSV
    ctPlateSoilStressK0 = St7API.ctPlateSoilStressK0
    ctPlateSoilStressSH = St7API.ctPlateSoilStressSH
    ctPlateSoilRatioOCR = St7API.ctPlateSoilRatioOCR
    ctPlateSoilRatioE0 = St7API.ctPlateSoilRatioE0
    ctPlateSoilFluidLevel = St7API.ctPlateSoilFluidLevel
    ctPlateAgeAtFirstLoading = St7API.ctPlateAgeAtFirstLoading


class PlateResultSubType(enum.Enum):
    stPlateLocal = St7API.stPlateLocal
    stPlateGlobal = St7API.stPlateGlobal
    stPlateCombined = St7API.stPlateCombined
    stPlateSupport = St7API.stPlateSupport
    stPlateDevLocal = St7API.stPlateDevLocal
    stPlateDevGlobal = St7API.stPlateDevGlobal
    stPlateDevCombined = St7API.stPlateDevCombined
    stPlateCavity = St7API.stPlateCavity


class PlateResultType(enum.Enum):
    rtPlateStress = St7API.rtPlateStress
    rtPlateStrain = St7API.rtPlateStrain
    rtPlateEnergyDensity = St7API.rtPlateEnergyDensity
    rtPlateForce = St7API.rtPlateForce
    rtPlateMoment = St7API.rtPlateMoment
    rtPlateCurvature = St7API.rtPlateCurvature
    rtPlatePlyStress = St7API.rtPlatePlyStress
    rtPlatePlyStrain = St7API.rtPlatePlyStrain
    rtPlatePlyReserve = St7API.rtPlatePlyReserve
    rtPlateFlux = St7API.rtPlateFlux
    rtPlateGradient = St7API.rtPlateGradient
    rtPlateRCDesign = St7API.rtPlateRCDesign
    rtPlateCreepStrain = St7API.rtPlateCreepStrain
    rtPlateSoil = St7API.rtPlateSoil
    rtPlateUser = St7API.rtPlateUser
    rtPlateNodeReact = St7API.rtPlateNodeReact
    rtPlateNodeDisp = St7API.rtPlateNodeDisp
    rtPlateNodeBirthDisp = St7API.rtPlateNodeBirthDisp
    rtPlateEffectiveStress = St7API.rtPlateEffectiveStress
    rtPlateEffectiveForce = St7API.rtPlateEffectiveForce
    rtPlateNodeFlux = St7API.rtPlateNodeFlux
    rtPlateTotalStrain = St7API.rtPlateTotalStrain
    rtPlateTotalCurvature = St7API.rtPlateTotalCurvature
    rtPlateEnergyIntegral = St7API.rtPlateEnergyIntegral


class PlateSurface(enum.Enum):
    psPlateMidPlane = St7API.psPlateMidPlane
    psPlateMinusZ = St7API.psPlateMinusZ
    psPlatePlusZ = St7API.psPlatePlusZ


class PreLoadType(enum.Enum):
    plBeamPreTension = St7API.plBeamPreTension
    plBeamPreStrain = St7API.plBeamPreStrain
    plPlatePreStress = St7API.plPlatePreStress
    plPlatePreStrain = St7API.plPlatePreStrain
    plBrickPreStress = St7API.plBrickPreStress
    plBrickPreStrain = St7API.plBrickPreStrain
    plCavityPreStress = St7API.plCavityPreStress
    plCavityPreStrain = St7API.plCavityPreStrain


class Property(enum.Enum):
    ptBEAMPROP = St7API.ptBEAMPROP
    ptPLATEPROP = St7API.ptPLATEPROP
    ptBRICKPROP = St7API.ptBRICKPROP
    ptPLYPROP = St7API.ptPLYPROP


class SampleLocation(enum.Enum):
    spCentroid = St7API.spCentroid
    spGaussPoints = St7API.spGaussPoints
    spNodesAverageNever = St7API.spNodesAverageNever
    spNodesAverageAll = St7API.spNodesAverageAll
    spNodesAverageSame = St7API.spNodesAverageSame


class ScaleType(enum.Enum):
    dsPercent = St7API.dsPercent
    dsAbsolute = St7API.dsAbsolute


class SolverDefaultInteger(enum.Enum):
    spTreeStartNumber = St7API.spTreeStartNumber
    spNumFrequency = St7API.spNumFrequency
    spNumBucklingModes = St7API.spNumBucklingModes
    spMaxIterationEig = St7API.spMaxIterationEig
    spMaxIterationNonlin = St7API.spMaxIterationNonlin
    spNumBeamSlicesModal = St7API.spNumBeamSlicesModal
    spMaxConjugateGradientIter = St7API.spMaxConjugateGradientIter
    spMaxNumRepeatedMessages = St7API.spMaxNumRepeatedMessages
    spFiniteStrainDefinition = St7API.spFiniteStrainDefinition
    spBeamLength = St7API.spBeamLength
    spFormStiffMatrix = St7API.spFormStiffMatrix
    spMaxUpdateInterval = St7API.spMaxUpdateInterval
    spFormNonlinHeatStiffMatrix = St7API.spFormNonlinHeatStiffMatrix
    spExpandWorkingSet = St7API.spExpandWorkingSet
    spMinNumViscoUnits = St7API.spMinNumViscoUnits
    spMaxNumViscoUnits = St7API.spMaxNumViscoUnits
    spCurveFitTimeUnit = St7API.spCurveFitTimeUnit
    spStaticAutoStepping = St7API.spStaticAutoStepping
    spBeamKgType = St7API.spBeamKgType
    spDynamicAutoStepping = St7API.spDynamicAutoStepping
    spMaxIterationHeat = St7API.spMaxIterationHeat


class SolverDefaultLogical(enum.Enum):
    spDoSturm = St7API.spDoSturm
    spNonlinearMaterial = St7API.spNonlinearMaterial
    spUnusedL3 = St7API.spUnusedL3
    spNonlinearGeometry = St7API.spNonlinearGeometry
    spUnusedL5 = St7API.spUnusedL5
    spAddKg = St7API.spAddKg
    spUnusedL7 = St7API.spUnusedL7
    spCalcDampingRatios = St7API.spCalcDampingRatios
    spIncludeLinkReactions = St7API.spIncludeLinkReactions
    spFullSystemTransient = St7API.spFullSystemTransient
    spNonlinearHeat = St7API.spNonlinearHeat
    spLumpedLoadBeam = St7API.spLumpedLoadBeam
    spLumpedLoadPlate = St7API.spLumpedLoadPlate
    spUnusedL14 = St7API.spUnusedL14
    spLumpedMassBeam = St7API.spLumpedMassBeam
    spLumpedMassPlate = St7API.spLumpedMassPlate
    spLumpedMassBrick = St7API.spLumpedMassBrick
    spForceSingularityCheck = St7API.spForceSingularityCheck
    spUnusedL19 = St7API.spUnusedL19
    spSaveRestartFile = St7API.spSaveRestartFile
    spSaveIntermediate = St7API.spSaveIntermediate
    spExcludeMassX = St7API.spExcludeMassX
    spExcludeMassY = St7API.spExcludeMassY
    spExcludeMassZ = St7API.spExcludeMassZ
    spSaveSRSSSpectral = St7API.spSaveSRSSSpectral
    spSaveCQCSpectral = St7API.spSaveCQCSpectral
    spDoResidualsCheck = St7API.spDoResidualsCheck
    spSuppressAllSingularities = St7API.spSuppressAllSingularities
    spAutoPCGIterations = St7API.spAutoPCGIterations
    spUnusedL30 = St7API.spUnusedL30
    spReducedLogFile = St7API.spReducedLogFile
    spIncludeRotationalMass = St7API.spIncludeRotationalMass
    spIgnoreCompressiveBeamKg = St7API.spIgnoreCompressiveBeamKg
    spAutoScaleKg = St7API.spAutoScaleKg
    spUnusedL35 = St7API.spUnusedL35
    spScaleSupports = St7API.spScaleSupports
    spAutoShift = St7API.spAutoShift
    spSaveTableInsertedSteps = St7API.spSaveTableInsertedSteps
    spSaveLastRestartStep = St7API.spSaveLastRestartStep
    spUnusedL40 = St7API.spUnusedL40
    spDoInstantNTA = St7API.spDoInstantNTA
    spAllowExtraIterations = St7API.spAllowExtraIterations
    spPredictImpact = St7API.spPredictImpact
    spAutoWorkingSet = St7API.spAutoWorkingSet
    spDampingForce = St7API.spDampingForce
    spLimitDisplacementNLA = St7API.spLimitDisplacementNLA
    spLimitRotationNLA = St7API.spLimitRotationNLA
    spSaveFinalSubStep = St7API.spSaveFinalSubStep
    spCablesAsMultiCase = St7API.spCablesAsMultiCase
    spShowMessages = St7API.spShowMessages
    spShowProgress = St7API.spShowProgress
    spShowConvergenceGraph = St7API.spShowConvergenceGraph
    spUnusedL53 = St7API.spUnusedL53
    spSpectralBaseExcitation = St7API.spSpectralBaseExcitation
    spSpectralLoadExcitation = St7API.spSpectralLoadExcitation
    spUnusedL56 = St7API.spUnusedL56
    spCheckEigenvector = St7API.spCheckEigenvector
    spAppendRemainingTime = St7API.spAppendRemainingTime
    spIncludeFollowerLoadKG = St7API.spIncludeFollowerLoadKG
    spInertiaForce = St7API.spInertiaForce
    spSolverGeneratesCombinations = St7API.spSolverGeneratesCombinations
    spAutoNewmarkAlpha = St7API.spAutoNewmarkAlpha


class SolverMode(enum.Enum):
    smNormalRun = St7API.smNormalRun
    smProgressRun = St7API.smProgressRun
    smBackgroundRun = St7API.smBackgroundRun
    smNormalCloseRun = St7API.smNormalCloseRun


class SolverType(enum.Enum):
    stLinearStatic = St7API.stLinearStatic
    stLinearBuckling = St7API.stLinearBuckling
    stNonlinearStatic = St7API.stNonlinearStatic
    stNaturalFrequency = St7API.stNaturalFrequency
    stHarmonicResponse = St7API.stHarmonicResponse
    stSpectralResponse = St7API.stSpectralResponse
    stLinearTransientDynamic = St7API.stLinearTransientDynamic
    stNonlinearTransientDynamic = St7API.stNonlinearTransientDynamic
    stSteadyHeat = St7API.stSteadyHeat
    stTransientHeat = St7API.stTransientHeat
    stLoadInfluence = St7API.stLoadInfluence
    stQuasiStatic = St7API.stQuasiStatic


class TableType(enum.Enum):
    ttVsTime = St7API.ttVsTime
    ttVsTemperature = St7API.ttVsTemperature
    ttVsFrequency = St7API.ttVsFrequency
    ttStressStrain = St7API.ttStressStrain
    ttForceDisplacement = St7API.ttForceDisplacement
    ttMomentCurvature = St7API.ttMomentCurvature
    ttMomentRotation = St7API.ttMomentRotation
    ttAccVsTime = St7API.ttAccVsTime
    ttForceVelocity = St7API.ttForceVelocity
    ttVsPosition = St7API.ttVsPosition
    ttStrainTime = St7API.ttStrainTime
    ttDispVsTime = St7API.ttDispVsTime
    ttVelVsTime = St7API.ttVelVsTime
    ttVsVelocity = St7API.ttVsVelocity
    ttTemperatureVsTime = St7API.ttTemperatureVsTime


class WindowsRefreshMode(enum.Enum):
    wrAutoRefresh = St7API.wrAutoRefresh
    wrPauseClear = St7API.wrPauseClear
    wrPauseNoClear = St7API.wrPauseNoClear
